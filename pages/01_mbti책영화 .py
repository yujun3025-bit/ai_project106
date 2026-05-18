import streamlit as st

st.set_page_config(
    page_title="MBTI 진로 추천 🎯",
    page_icon="✨",
    layout="centered"
)

# MBTI별 진로 데이터
career_data = {
    "INTJ": [
        {
            "job": "🧠 데이터 사이언티스트",
            "major": "컴퓨터공학과, 인공지능학과",
            "personality": "분석적이고 전략 세우는 걸 좋아하는 사람!",
            "salary": "평균 연봉 약 5,500만원"
        },
        {
            "job": "📊 경영 컨설턴트",
            "major": "경영학과, 경제학과",
            "personality": "문제 해결 능력이 뛰어나고 계획적인 사람!",
            "salary": "평균 연봉 약 6,000만원"
        }
    ],

    "INTP": [
        {
            "job": "💻 프로그래머",
            "major": "소프트웨어학과, 컴퓨터공학과",
            "personality": "호기심 많고 논리적인 사람!",
            "salary": "평균 연봉 약 5,000만원"
        },
        {
            "job": "🔬 연구원",
            "major": "물리학과, 화학과",
            "personality": "탐구심이 강하고 아이디어가 많은 사람!",
            "salary": "평균 연봉 약 4,800만원"
        }
    ],

    "ENTJ": [
        {
            "job": "🏢 CEO",
            "major": "경영학과, 경제학과",
            "personality": "리더십 강하고 목표 지향적인 사람!",
            "salary": "평균 연봉 약 7,000만원"
        },
        {
            "job": "📈 마케팅 기획자",
            "major": "광고홍보학과, 경영학과",
            "personality": "도전 정신이 강하고 추진력 있는 사람!",
            "salary": "평균 연봉 약 5,200만원"
        }
    ],

    "ENTP": [
        {
            "job": "🚀 스타트업 창업가",
            "major": "경영학과, 산업공학과",
            "personality": "새로운 아이디어를 좋아하는 사람!",
            "salary": "평균 연봉 약 6,000만원"
        },
        {
            "job": "🎤 방송 PD",
            "major": "미디어학과, 영상학과",
            "personality": "창의적이고 말하는 걸 좋아하는 사람!",
            "salary": "평균 연봉 약 4,700만원"
        }
    ],

    "INFJ": [
        {
            "job": "💖 심리상담사",
            "major": "심리학과, 상담학과",
            "personality": "공감 능력이 뛰어난 사람!",
            "salary": "평균 연봉 약 4,200만원"
        },
        {
            "job": "📚 작가",
            "major": "문예창작과, 국어국문학과",
            "personality": "상상력이 풍부하고 감성적인 사람!",
            "salary": "평균 연봉 약 4,000만원"
        }
    ],

    "INFP": [
        {
            "job": "🎨 일러스트레이터",
            "major": "디자인학과, 미술학과",
            "personality": "감수성이 풍부하고 창의적인 사람!",
            "salary": "평균 연봉 약 4,000만원"
        },
        {
            "job": "🎵 음악 프로듀서",
            "major": "실용음악과",
            "personality": "자기 표현을 좋아하는 사람!",
            "salary": "평균 연봉 약 4,500만원"
        }
    ],

    "ENFJ": [
        {
            "job": "👩‍🏫 교사",
            "major": "교육학과",
            "personality": "사람들을 도와주는 걸 좋아하는 사람!",
            "salary": "평균 연봉 약 5,000만원"
        },
        {
            "job": "🤝 HR 담당자",
            "major": "경영학과, 심리학과",
            "personality": "소통 능력이 뛰어난 사람!",
            "salary": "평균 연봉 약 4,800만원"
        }
    ],

    "ENFP": [
        {
            "job": "📺 유튜버",
            "major": "미디어학과, 방송연예과",
            "personality": "에너지 넘치고 끼 많은 사람!",
            "salary": "평균 연봉 다양함 😆"
        },
        {
            "job": "🎉 이벤트 기획자",
            "major": "관광경영학과, 경영학과",
            "personality": "사람 만나는 걸 좋아하는 사람!",
            "salary": "평균 연봉 약 4,300만원"
        }
    ],

    "ISTJ": [
        {
            "job": "🏦 회계사",
            "major": "회계학과, 세무학과",
            "personality": "꼼꼼하고 책임감 강한 사람!",
            "salary": "평균 연봉 약 6,500만원"
        },
        {
            "job": "⚖️ 공무원",
            "major": "행정학과",
            "personality": "안정적이고 성실한 사람!",
            "salary": "평균 연봉 약 4,500만원"
        }
    ],

    "ISFJ": [
        {
            "job": "🏥 간호사",
            "major": "간호학과",
            "personality": "배려심 많고 따뜻한 사람!",
            "salary": "평균 연봉 약 4,700만원"
        },
        {
            "job": "👶 유치원 교사",
            "major": "유아교육과",
            "personality": "인내심이 강한 사람!",
            "salary": "평균 연봉 약 3,800만원"
        }
    ],

    "ESTJ": [
        {
            "job": "📋 프로젝트 매니저",
            "major": "경영학과",
            "personality": "체계적이고 리더십 있는 사람!",
            "salary": "평균 연봉 약 5,800만원"
        },
        {
            "job": "👮 경찰관",
            "major": "경찰행정학과",
            "personality": "정의감이 강한 사람!",
            "salary": "평균 연봉 약 4,900만원"
        }
    ],

    "ESFJ": [
        {
            "job": "✈️ 승무원",
            "major": "항공서비스학과",
            "personality": "친절하고 사교적인 사람!",
            "salary": "평균 연봉 약 5,000만원"
        },
        {
            "job": "🏨 호텔리어",
            "major": "호텔관광학과",
            "personality": "서비스 정신이 뛰어난 사람!",
            "salary": "평균 연봉 약 4,300만원"
        }
    ],

    "ISTP": [
        {
            "job": "🔧 자동차 엔지니어",
            "major": "기계공학과",
            "personality": "손재주 좋고 현실적인 사람!",
            "salary": "평균 연봉 약 5,500만원"
        },
        {
            "job": "🛠️ 파일럿",
            "major": "항공운항학과",
            "personality": "침착하고 집중력 강한 사람!",
            "salary": "평균 연봉 약 7,000만원"
        }
    ],

    "ISFP": [
        {
            "job": "📷 사진작가",
            "major": "사진영상학과",
            "personality": "감각적이고 자유로운 사람!",
            "salary": "평균 연봉 약 4,000만원"
        },
        {
            "job": "💄 메이크업 아티스트",
            "major": "뷰티미용학과",
            "personality": "예술 감각이 뛰어난 사람!",
            "salary": "평균 연봉 약 3,800만원"
        }
    ],

    "ESTP": [
        {
            "job": "💼 영업 전문가",
            "major": "경영학과",
            "personality": "활동적이고 자신감 있는 사람!",
            "salary": "평균 연봉 약 5,300만원"
        },
        {
            "job": "🏀 스포츠 마케터",
            "major": "스포츠산업학과",
            "personality": "도전 정신 강한 사람!",
            "salary": "평균 연봉 약 4,500만원"
        }
    ],

    "ESFP": [
        {
            "job": "🎬 배우",
            "major": "연극영화과",
            "personality": "표현력이 풍부한 사람!",
            "salary": "평균 연봉 다양함 🌟"
        },
        {
            "job": "🎤 방송인",
            "major": "방송연예과",
            "personality": "사람들 앞에서 빛나는 사람!",
            "salary": "평균 연봉 약 5,000만원"
        }
    ]
}

# 제목
st.title("✨ MBTI 진로 추천 서비스 ✨")
st.write("나의 MBTI에 딱 맞는 직업을 찾아보자 😎")

# MBTI 선택
mbti = st.selectbox(
    "👉 너의 MBTI를 선택해줘!",
    list(career_data.keys())
)

st.divider()

# 결과 출력
st.subheader(f"🎯 {mbti} 유형 추천 진로")

for career in career_data[mbti]:
    st.markdown(f"""
    ### {career['job']}
    
    🎓 **추천 학과**  
    {career['major']}
    
    💡 **잘 맞는 성격**  
    {career['personality']}
    
    💰 **평균 연봉**  
    {career['salary']}
    
    ---
    """)

st.success("🌈 미래의 멋진 너를 응원할게!")
