import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import platform

# ---------------------------
# 한글 폰트 설정
# ---------------------------
if platform.system() == 'Windows':
    plt.rc('font', family='Malgun Gothic')
elif platform.system() == 'Darwin':
    plt.rc('font', family='AppleGothic')
else:
    plt.rc('font', family='NanumGothic')

plt.rcParams['axes.unicode_minus'] = False

# ---------------------------
# 데이터 불러오기
# ---------------------------
df = pd.read_csv("population.csv", encoding='cp949')

# 컬럼 정리
df.columns = df.columns.str.strip()

# 지역명 컬럼 찾기
region_col = df.columns[0]

# 총인구 제외하고 나이 컬럼만 가져오기
age_columns = df.columns[2:]

# ---------------------------
# Streamlit UI
# ---------------------------
st.title("서울시 연령별 인구 분석")

# 행정구 선택
selected_region = st.selectbox(
    "행정구를 선택하세요",
    df[region_col]
)

# 선택한 지역 데이터
region_data = df[df[region_col] == selected_region]

# 나이 / 인구 데이터 추출
ages = []
population = []

for col in age_columns:
    try:
        age = int(col.replace('세', '').replace(' 이상', ''))
        value = int(str(region_data[col].values[0]).replace(',', ''))
        
        ages.append(age)
        population.append(value)
    except:
        continue

# ---------------------------
# 그래프 그리기
# ---------------------------
fig, ax = plt.subplots(figsize=(14, 6))

ax.plot(
    ages,
    population,
    color='hotpink',
    linewidth=2
)

# 제목 및 축
ax.set_title(f"{selected_region} 연령별 인구수", fontsize=18)
ax.set_xlabel("나이", fontsize=12)
ax.set_ylabel("인구수", fontsize=12)

# x축 10살 단위 표시
ax.set_xticks(range(0, 101, 10))

# 세로 구분선
ax.grid(axis='x', linestyle='--', alpha=0.5)

# Streamlit 출력
st.pyplot(fig)
