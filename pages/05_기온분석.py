import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="서울 기온 분석",
    layout="wide"
)

st.title("🌡️ 서울 기온 연도별 분석")

uploaded_file = st.file_uploader(
    "seoul.csv 파일 업로드",
    type=["csv"]
)

if uploaded_file is not None:

    # CSV 읽기
    try:
        df = pd.read_csv(uploaded_file, encoding="cp949")
    except:
        try:
            df = pd.read_csv(uploaded_file, encoding="utf-8")
        except:
            df = pd.read_csv(uploaded_file, encoding="euc-kr")

    # 컬럼명 공백 제거
    df.columns = df.columns.str.strip()

    # 날짜 컬럼 찾기
    date_col = None

    for col in df.columns:
        if "날짜" in col:
            date_col = col
            break

    if date_col is None:
        st.error("날짜 컬럼을 찾을 수 없습니다.")
        st.stop()

    # 날짜 변환
    df[date_col] = pd.to_datetime(
        df[date_col],
        errors="coerce"
    )

    # 날짜 없는 행 제거
    df = df.dropna(subset=[date_col])

    # 연도 월 일 생성
    df["연도"] = df[date_col].dt.year
    df["월"] = df[date_col].dt.month
    df["일"] = df[date_col].dt.day

    # 최고기온 컬럼 찾기
    max_col = None
    min_col = None

    for col in df.columns:
        if "최고기온" in col:
            max_col = col

        if "최저기온" in col:
            min_col = col

    if max_col is None or min_col is None:
        st.error("최고기온 또는 최저기온 컬럼을 찾을 수 없습니다.")
        st.stop()

    # 숫자 변환
    df[max_col] = pd.to_numeric(
        df[max_col],
        errors="coerce"
    )

    df[min_col] = pd.to_numeric(
        df[min_col],
        errors="coerce"
    )

    # 월 선택
    month = st.selectbox(
        "월 선택",
        range(1, 13)
    )

    # 일 선택
    day = st.selectbox(
        "일 선택",
        range(1, 32)
    )

    filtered = df[
        (df["월"] == month)
        & (df["일"] == day)
    ].copy()

    filtered = filtered.sort_values("연도")

    if len(filtered) == 0:
        st.warning("선택한 날짜 데이터가 없습니다.")
    else:

        fig, ax = plt.subplots(
            figsize=(14, 6)
        )

        ax.plot(
            filtered["연도"],
            filtered[max_col],
            color="hotpink",
            linewidth=2,
            marker="o",
            label="최고기온"
        )

        ax.plot(
            filtered["연도"],
            filtered[min_col],
            color="lightskyblue",
            linewidth=2,
            marker="o",
            label="최저기온"
        )

        ax.set_title(
            f"{month}월 {day}일 연도별 최고·최저기온 변화",
            fontsize=16
        )

        ax.set_xlabel("연도")
        ax.set_ylabel("기온(℃)")

        ax.legend()

        ax.grid(
            True,
            linestyle="--",
            alpha=0.4
        )

        st.pyplot(fig)

        st.subheader("선택한 날짜 데이터")

        st.dataframe(
            filtered[
                ["연도", max_col, min_col]
            ],
            use_container_width=True
        )
