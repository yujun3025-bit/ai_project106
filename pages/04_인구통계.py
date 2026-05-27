import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import platform
import re

# -----------------------------------
# 페이지 설정
# -----------------------------------
st.set_page_config(
    page_title="서울시 연령별 인구 분석",
    layout="wide"
)

# -----------------------------------
# 한글 폰트 설정
# -----------------------------------
if platform.system() == "Windows":
    plt.rc("font", family="Malgun Gothic")
elif platform.system() == "Darwin":
    plt.rc("font", family="AppleGothic")
else:
    plt.rc("font", family="NanumGothic")

plt.rcParams["axes.unicode_minus"] = False

# -----------------------------------
# 제목
# -----------------------------------
st.title("서울시 연령별 인구 분석")

# -----------------------------------
# CSV 파일 불러오기
# -----------------------------------
try:
    df = pd.read_csv("population.csv", encoding="cp949")
except:
    df = pd.read_csv("population.csv", encoding="utf-8")

# 컬럼 공백 제거
df.columns = df.columns.str.strip()

# -----------------------------------
# 지역 컬럼 찾기
# -----------------------------------
region_col = df.columns[0]

# -----------------------------------
# 나이 컬럼만 추출
# -----------------------------------
age_columns = []

for col in df.columns:

    # "0세", "1세", "100세 이상" 같은 컬럼만 선택
    if "세" in col:

        # 숫자 추출
        numbers = re.findall(r"\d+", col)

        if len(numbers) > 0:
            age_columns.append(col)

# -----------------------------------
# 행정구 선택
# -----------------------------------
selected_region = st.selectbox(
    "행정구 선택",
    df[region_col].unique()
)

# -----------------------------------
# 선택된 지역 데이터
# -----------------------------------
selected_data = df[df[region_col] == selected_region]

# -----------------------------------
# 그래프용 데이터 생성
# -----------------------------------
ages = []
populations = []

for col in age_columns:

    try:
        # 나이 숫자 추출
        age = int(re.findall(r"\d+", col)[0])

        # 인구수 추출
        value = selected_data[col].values[0]

        # 쉼표 제거
        value = str(value).replace(",", "")

        population = int(float(value))

        ages.append(age)
        populations.append(population)

    except:
        continue

# -----------------------------------
# 데이터프레임 생성 및 정렬
# -----------------------------------
graph_df = pd.DataFrame({
    "나이": ages,
    "인구수": populations
})

graph_df = graph_df.sort_values("나이")

# -----------------------------------
# 그래프 생성
# -----------------------------------
fig, ax = plt.subplots(figsize=(18, 8))

# 꺾은선 그래프
ax.plot(
    graph_df["나이"],
    graph_df["인구수"],
    color="hotpink",
    linewidth=3
)

# -----------------------------------
# 축 설정
# -----------------------------------

# x축 범위
ax.set_xlim(0, 100)

# y축 범위 자동 조절
ax.set_ylim(0, graph_df["인구수"].max() * 1.1)

# x축 눈금
ax.set_xticks(range(0, 101, 10))

# 축 이름
ax.set_xlabel("나이", fontsize=16)
ax.set_ylabel("인구수", fontsize=16)

# 제목
ax.set_title(
    f"{selected_region} 연령별 인구수",
    fontsize=24
)

# -----------------------------------
# 세로 구분선
# -----------------------------------
ax.grid(
    axis="x",
    linestyle="--",
    alpha=0.5
)

# -----------------------------------
# 그래프 스타일
# -----------------------------------
ax.tick_params(axis='x', labelsize=12)
ax.tick_params(axis='y', labelsize=12)

# 여백 자동 조정
plt.tight_layout()

# -----------------------------------
# Streamlit 출력
# -----------------------------------
st.pyplot(fig)

# -----------------------------------
# 데이터 표 출력
# -----------------------------------
st.subheader("연령별 인구 데이터")

st.dataframe(
    graph_df,
    use_container_width=True
)
