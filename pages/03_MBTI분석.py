# app.py

```python
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# 페이지 설정
st.set_page_config(page_title="국가별 MBTI 분석", layout="wide")

# 제목
st.title("🌍 국가별 MBTI 비율 분석")
st.write("국가를 선택하면 MBTI 비율을 막대그래프로 확인할 수 있습니다.")

# 데이터 불러오기
@st.cache_data

def load_data():
    return pd.read_csv("countriesMBTI_16types.csv")


df = load_data()

# 국가 선택
countries = sorted(df["Country"].unique())
selected_country = st.selectbox("국가를 선택하세요", countries)

# 선택 국가 데이터
country_data = df[df["Country"] == selected_country].iloc[0]

# MBTI 데이터 추출
mbti_data = country_data.drop("Country")
mbti_data = mbti_data.sort_values(ascending=False)

# 최고 비율 MBTI
max_type = mbti_data.idxmax()

# 색상 설정
colors = []

# 하늘색 그라데이션 생성
base_color = np.array([135, 206, 250]) / 255  # skyblue
white = np.array([1, 1, 1])

for i, mbti in enumerate(mbti_data.index):
    if mbti == max_type:
        colors.append("yellow")
    else:
        ratio = i / len(mbti_data)
        gradient = base_color * (1 - ratio) + white * ratio
        colors.append(gradient)

# 그래프 생성
fig, ax = plt.subplots(figsize=(12, 6))

bars = ax.bar(mbti_data.index, mbti_data.values, color=colors)

# 그래프 스타일
ax.set_title(f"{selected_country} MBTI 비율", fontsize=18)
ax.set_xlabel("MBTI 유형", fontsize=12)
ax.set_ylabel("비율", fontsize=12)
ax.set_ylim(0, mbti_data.max() * 1.2)

# 값 표시
for bar in bars:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.2%}",
        ha="center",
        va="bottom",
        fontsize=9,
    )

st.pyplot(fig)

# 최고 비율 MBTI 표시
st.success(f"🏆 {selected_country}에서 가장 높은 MBTI는 {max_type} 입니다!")
```

---

# requirements.txt

```txt
streamlit
pandas
matplotlib
numpy
```

---

# Streamlit Cloud 배포 방법

1. GitHub에 아래 파일 업로드

   * app.py
   * requirements.txt
   * countriesMBTI_16types.csv

2. Streamlit Cloud 접속

3. GitHub 저장소 연결 후 배포

4. 메인 파일은 `app.py` 선택

5. Deploy 버튼 클릭
