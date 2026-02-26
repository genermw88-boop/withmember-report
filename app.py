import streamlit as st
from datetime import datetime

st.set_page_config(page_title="WithMember Report", layout="wide")

# 사이드바 입력
with st.sidebar:
    st.title("🛠️ 리포트 설정")
    store_name = st.text_input("매장명", "봉천동 콤마")
    report_month = st.selectbox("월 선택", [f"{i}월" for i in range(1, 13)], index=1)
    curr_clicks = st.number_input("이번달 클릭수", value=650)
    new_reviews = st.number_input("이번달 신규 리뷰", value=25)
    insta_views = st.number_input("인스타 조회수", value=1500)

st.title("📑 위드멤버 성과 리포트")

if st.button("✨ 리포트 발행"):
    # HTML 디자인 정의
    report_html = f"""
    <div style="background: white; padding: 25px; border-radius: 15px; border: 1px solid #eee; box-shadow: 0 4px 10px rgba(0,0,0,0.1);">
        <h2 style="color: #1e3a8a;">{report_month} 성과 보고서: {store_name}</h2>
        <hr>
        <p>✅ <b>네이버 클릭수:</b> {curr_clicks:,}회</p>
        <p>✅ <b>신규 리뷰:</b> {new_reviews}건 등록 완료</p>
        <p>✅ <b>인스타 노출:</b> {insta_views:,}회 달성</p>
        <br>
        <p style="color: #666;">위드멤버 마케팅 분석 시스템에 의해 생성되었습니다.</p>
    </div>
    """
    
    # [가장 중요] HTML로 화면에 출력하기
    st.markdown(report_html, unsafe_allow_html=True)
else:
    st.info("왼쪽 데이터를 확인하고 버튼을 눌러주세요.")
