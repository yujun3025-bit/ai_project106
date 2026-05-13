import streamlit as st
st.title('나의 첫 서비스 만들기!')
st.text_input('이름을 입력하세요')
st.selectbox('좋아하는 사람을 선택하세요',['떡볶이','치킨','마라탕'])
st.button('인사말 생성')
