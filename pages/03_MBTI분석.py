import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# 페이지 설정
st.set_page_config(
    page_title="국가별 MBTI 분석",
    layout="wide"
)

# 제목
st.title("🌍 국가별 MBTI 분석 대시보드")

# 데이터 불러오기
@st.cache_data
def load_data():
    return pd.read_csv("countriesMBTI_16types.csv")

df = load_data()

# -------------------------------
# 국가 선택 영역
# -------------------------------

st.header("1️⃣ 국가별 MBTI 비율 보기")

countries = sorted(df["Country"].unique())

selected_country = st.selectbox(
    "국가를 선택하세요",
    countries
)

# 선택 국가 데이터
country_data = df[df["Country"] == selected_country].iloc[0]

# MBTI 데이터만 추출
mbti_data = country_data.drop("Country")
mbti_data = mbti_data.sort_values(ascending=False)

# 최고 MBTI
max_type = mbti_data.idxmax()

# -------------------------------
# 초록색 그라데이션 색상 생성
# -------------------------------

colors = []

# 진한 초록
base_green = np.array([34, 139, 34]) / 255

# 밝은 초록
light_green = np.array([220, 255, 220]) / 255

for i, mbti in enumerate(mbti_data.index):

    # 1등은 금색
    if mbti == max_type:
        colors.append("gold")

    else:
        ratio = i / len(mbti_data)

        gradient = (
            base_green * (1 - ratio)
            + light_green * ratio
        )

        colors.append(gradient)

# -------------------------------
# 그래프 생성
# -------------------------------

fig, ax = plt.subplots(figsize=(12, 6))

bars = ax.bar(
    mbti_data.index,
    mbti_data.values,
    color=colors
)

# 제목 및 축
ax.set_title(
    f"{selected_country} MBTI 비율",
    fontsize=18
)

ax.set_xlabel("MBTI 유형")
ax.set_ylabel("비율")

# 값 표시
for bar in bars:

    height = bar.get_height()

    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.2%}",
        ha="center",
        va="bottom",
        fontsize=9
    )

# Streamlit 출력
st.pyplot(fig)

st.success(
    f"🏆 {selected_country}에서 가장 높은 MBTI는 {max_type} 입니다!"
)

# -------------------------------
# MBTI TOP 10 국가 기능
# -------------------------------

st.header("2️⃣ MBTI별 높은 비율 국가 TOP 10")

mbti_types = list(df.columns[1:])

selected_mbti = st.selectbox(
    "MBTI를 선택하세요",
    mbti_types
)

# 선택 MBTI 기준 정렬
top10 = df[["Country", selected_mbti]] \
    .sort_values(
        by=selected_mbti,
        ascending=False
    ) \
    .head(10)

# 순위 추가
top10 = top10.reset_index(drop=True)
top10.index = top10.index + 1

# 표 출력
st.subheader(f"🏅 {selected_mbti} 비율 TOP 10 국가")

st.dataframe(
    top10,
    use_container_width=True
)

# -------------------------------
# TOP10 그래프
# -------------------------------

fig2, ax2 = plt.subplots(figsize=(12, 6))

# 초록 그라데이션
top_colors = []

for i in range(len(top10)):

    if i == 0:
        top_colors.append("gold")

    else:
        ratio = i / len(top10)

        gradient = (
            base_green * (1 - ratio)
            + light_green * ratio
        )

        top_colors.append(gradient)

bars2 = ax2.bar(
    top10["Country"],
    top10[selected_mbti],
    color=top_colors
)

ax2.set_title(
    f"{selected_mbti} 비율 TOP 10 국가",
    fontsize=18
)

ax2.set_xlabel("국가")
ax2.set_ylabel("비율")

plt.xticks(rotation=45)

# 값 표시
for bar in bars2:

    height = bar.get_height()

    ax2.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.2%}",
        ha="center",
        va="bottom",
        fontsize=9
    )

st.pyplot(fig2)
