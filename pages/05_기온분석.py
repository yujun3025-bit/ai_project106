import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="서울 기온 분석", layout="wide")

st.title("서울 기온 연도별 최고·최저기온 분석")

uploaded_file = st.file_uploader(
    "seoul.csv 파일을 업로드하세요",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(
        uploaded_file,
        encoding="cp949"
    )

    # 컬럼명 공백 제거
    df.columns = df.columns.str.strip()

    # 날짜 변환
    df["날짜"] = pd.to_datetime(df["날짜"])

    # 연도, 월, 일 생성
    df["연도"] = df["날짜"].dt.year
    df["월"] = df["날짜"].dt.month
    df["일"] = df["날짜"].dt.day

    month = st.selectbox(
        "월 선택",
        range(1, 13)
    )

    day = st.selectbox(
        "일 선택",
        range(1, 32)
    )

    filtered = df[
        (df["월"] == month) &
        (df["일"] == day)
    ].copy()

    if len(filtered) == 0:
        st.warning("해당 날짜 데이터가 없습니다.")
    else:

        filtered = filtered.sort_values("연도")

        fig, ax = plt.subplots(figsize=(12, 6))

        ax.plot(
            filtered["연도"],
            filtered["최고기온(℃)"],
            color="hotpink",
            linewidth=2,
            label="최고기온"
        )

        ax.plot(
            filtered["연도"],
            filtered["최저기온(℃)"],
            color="lightskyblue",
            linewidth=2,
            label="최저기온"
        )

        ax.set_title(
            f"{month}월 {day}일 연도별 최고·최저기온 변화",
            fontsize=15
        )

        ax.set_xlabel("연도")
        ax.set_ylabel("기온(℃)")

        ax.grid(True, alpha=0.3)

        ax.legend()

        st.pyplot(fig)

        st.subheader("데이터 보기")
        st.dataframe(
            filtered[
                ["연도", "최고기온(℃)", "최저기온(℃)"]
            ],
            use_container_width=True
        )
