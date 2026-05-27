import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import platform
import re

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="서울시 연령별 인구 그래프",
    layout="wide"
)

# -----------------------------
# 한글 폰트 설정
# -----------------------------
if platform.system() == "Windows":
    plt.rc("font", family="Malgun Gothic")
elif platform.system() == "Darwin":
    plt.rc("font", family="AppleGothic")
else:
    plt.rc("font", family="NanumGothic")

plt.rcParams["axes.unicode_minus"] = False

# -----------------------------
# 제목
# -----------------------------
st.title("서울시 연령별 인구 분석")

# -----------------------------
# CSV 불러오기
# -----------------------------
try:
    df = pd.read_csv("population.csv", encoding="cp949")
except:
    df = pd.read_csv("population.csv", encoding="utf-8")

# 컬럼 공백 제거
df.columns = df.columns.str.strip()

# -----------------------------
# 지역 컬럼 찾기
# -----------------------------
region_col = df.columns[0]

# -----------------------------
# 나이 컬럼 찾기
# -----------------------------
age_columns = []

for col in df.columns:

    # "0세", "1세", "100세 이상" 형태 찾기
    if "세" in col:
        age_columns.append(col)

# -----------------------------
# 행정구 선택
# -----------------------------
selected_region = st.selectbox(
    "행정구 선택",
    df[region_col].tolist()
)

# 선택된 지역 데이터
region_data = df[df[region_col] == selected_region]

# -----------------------------
# 나이 / 인구 데이터 추출
# -----------------------------
ages = []
populations = []

for col in age_columns:

    # 숫자만 추출
    match = re.findall(r"\d+", col)

    if len(match) == 0:
        continue

    age = int(match[0])

    try:
        value = region_data[col].values[0]

        # 쉼표 제거
        value = str(value).replace(",", "")

        population = int(float(value))

        ages.append(age)
        populations.append(population)

    except:
        continue

# -----------------------------
# 데이터 정렬
# -----------------------------
chart_df = pd.DataFrame({
    "나이": ages,
    "인구수": populations
})

chart_df = chart_df.sort_values("나이")

# -----------------------------
# 그래프 생성
# -----------------------------
fig, ax = plt.subplots(figsize=(16, 7))

# 꺾은선 그래프
ax.plot(
    chart_df["나이"],
    chart_df["인구수"],
    color="hotpink",
    linewidth=3
)

# 제목
ax.set_title(
    f"{selected_region} 연령별 인구수",
    fontsize=22
)

# 가로축 / 세로축
ax.set_xlabel("나이", fontsize=15)
ax.set_ylabel("인구수", fontsize=15)

# x축 10살 단위
ax.set_xticks(range(0, 101, 10))

# 세로 구분선
ax.grid(
    axis="x",
    linestyle="--",
    alpha=0.5
)

# 여백 자동 조정
plt.tight_layout()

# Streamlit 출력
st.pyplot(fig)

# -----------------------------
# 데이터 보기
# -----------------------------
st.subheader("연령별 데이터")

st.dataframe(
    chart_df,
    use_container_width=True
)
