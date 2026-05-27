import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import platform

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="서울시 연령별 인구 분석",
    layout="wide"
)

# -----------------------------
# 한글 폰트 설정
# -----------------------------
if platform.system() == 'Windows':
    plt.rc('font', family='Malgun Gothic')
elif platform.system() == 'Darwin':
    plt.rc('font', family='AppleGothic')
else:
    plt.rc('font', family='NanumGothic')

plt.rcParams['axes.unicode_minus'] = False

# -----------------------------
# 제목
# -----------------------------
st.title("서울시 연령별 인구 분석")

# -----------------------------
# 데이터 불러오기
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

# 총인구 컬럼 제외
age_columns = []

for col in df.columns:
    if '세' in col:
        age_columns.append(col)

# -----------------------------
# 행정구 선택
# -----------------------------
selected_region = st.selectbox(
    "행정구를 선택하세요",
    df[region_col].tolist()
)

# 선택된 데이터
region_data = df[df[region_col] == selected_region]

# -----------------------------
# 나이 / 인구 데이터 추출
# -----------------------------
ages = []
population = []

for col in age_columns:

    # 컬럼 이름에서 숫자만 추출
    age_text = ''.join(filter(str.isdigit, col))

    if age_text == '':
        continue

    age = int(age_text)

    try:
        value = region_data[col].values[0]

        # 쉼표 제거
        value = str(value).replace(',', '')

        population_value = int(float(value))

        ages.append(age)
        population.append(population_value)

    except:
        continue

# -----------------------------
# 그래프 생성
# -----------------------------
fig, ax = plt.subplots(figsize=(15, 6))

ax.plot(
    ages,
    population,
    color='hotpink',
    linewidth=3
)

# 제목
ax.set_title(
    f"{selected_region} 연령별 인구수",
    fontsize=20
)

# 축 이름
ax.set_xlabel("나이", fontsize=14)
ax.set_ylabel("인구수", fontsize=14)

# x축 10살 단위
ax.set_xticks(range(0, 101, 10))

# 세로 구분선
ax.grid(
    axis='x',
    linestyle='--',
    alpha=0.5
)

# 배경
ax.set_facecolor('#fffafa')

# Streamlit 출력
st.pyplot(fig)

# -----------------------------
# 데이터 표 보기
# -----------------------------
st.subheader("데이터 보기")

chart_df = pd.DataFrame({
    "나이": ages,
    "인구수": population
})

st.dataframe(chart_df, use_container_width=True)
