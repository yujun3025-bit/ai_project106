import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(
    page_title="서울 인기 관광지 TOP10",
    layout="wide"
)

st.title("📍 외국인들이 좋아하는 서울 주요 관광지 TOP10")
st.markdown("Folium 지도로 서울의 대표 관광지를 확인하세요.")
