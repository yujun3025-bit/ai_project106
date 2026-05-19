import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(
    page_title="서울 인기 관광지 TOP10",
    layout="wide"
)

st.title("📍 외국인들이 좋아하는 서울 주요 관광지 TOP10")
st.markdown("Folium 지도로 서울의 대표 관광지를 확인하세요.")

# 서울 중심 좌표
seoul_map = folium.Map(
    location=[37.5665, 126.9780],
    zoom_start=11,
    tiles="CartoDB positron"
)

# 관광지 데이터
tourist_spots = [
    {
        "name": "경복궁",
        "lat": 37.579617,
        "lon": 126.977041,
        "desc": "조선 시대 대표 궁궐"
    },
    {
        "name": "북촌한옥마을",
        "lat": 37.582604,
        "lon": 126.983998,
        "desc": "전통 한옥 거리"
    },
    {
        "name": "명동",
        "lat": 37.563757,
        "lon": 126.985302,
        "desc": "쇼핑과 길거리 음식의 중심지"
    },
    {
        "name": "N서울타워",
        "lat": 37.551169,
        "lon": 126.988227,
        "desc": "서울 야경 명소"
    },
    {
        "name": "홍대거리",
        "lat": 37.556336,
        "lon": 126.922652,
        "desc": "젊음과 예술의 거리"
    },
    {
        "name": "인사동",
        "lat": 37.574187,
        "lon": 126.984956,
        "desc": "전통 문화 거리"
    },
    {
        "name": "동대문디자인플라자(DDP)",
        "lat": 37.566526,
        "lon": 127.009223,
        "desc": "현대 건축과 패션 중심지"
    },
    {
        "name": "롯데월드타워",
        "lat": 37.513068,
        "lon": 127.102926,
        "desc": "서울 랜드마크 초고층 빌딩"
    },
    {
        "name": "한강공원",
        "lat": 37.528316,
        "lon": 126.932651,
        "desc": "서울 시민들의 휴식 공간"
    },
    {
        "name": "광장시장",
        "lat": 37.570435,
        "lon": 126.999588,
        "desc": "한국 전통 음식 시장"
    }
]

# 마커 추가
for idx, spot in enumerate(tourist_spots, start=1):
    popup_html = f"""
    <b>{idx}. {spot['name']}</b><br>
    {spot['desc']}
    """

    folium.Marker(
        location=[spot["lat"], spot["lon"]],
        popup=popup_html,
        tooltip=spot["name"],
        icon=folium.Icon(
            color="blue",
            icon="info-sign"
        )
    ).add_to(seoul_map)

# 지도 출력
st_folium(
    seoul_map,
    width=1200,
    height=700
)

# 관광지 리스트
st.subheader("📌 관광지 목록")

for idx, spot in enumerate(tourist_spots, start=1):
    st.write(f"{idx}. {spot['name']} - {spot['desc']}")
