import streamlit as st
from datetime import datetime

# 1. 페이지 설정
st.set_page_config(page_title="WithMember Premium Report", layout="wide")

# 2. 사이드바 입력 (항목 누락 없도록 모두 포함)
with st.sidebar:
    st.header("🏢 기본 정보")
    store_name = st.text_input("매장명", value="봉천동 콤마")
    report_month = st.selectbox("리포트 월", [f"{i}월" for i in range(1, 13)], index=1)
    
    st.header("📍 네이버 데이터")
    last_clicks = st.number_input("지난달 클릭수", value=500)
    curr_clicks = st.number_input("이번달 클릭수", value=650)
    last_reviews = st.number_input("지난달 총 리뷰 수", value=100)
    curr_reviews = st.number_input("이번달 총 리뷰 수", value=125)

    st.header("📸 인스타그램 데이터")
    insta_views = st.number_input("조회수(노출)", value=1500)
    insta_eng = st.number_input("좋아요/댓글 합계", value=150)
    
    special_note = st.text_area("📢 분석 메모", "전체적인 지표 우상향 중")

# 3. 메인 화면 및 리포트 생성
st.title("📑 통합 마케팅 성과 리포트")

if st.button("✨ 프리미엄 리포트 발행"):
    # 데이터 계산
    click_diff = curr_clicks - last_clicks
    click_pct = (click_diff / last_clicks * 100) if last_clicks > 0 else 0
    new_reviews = curr_reviews - last_reviews

    # 디자인 (오류 방지를 위해 텍스트 형식을 더 안전하게 변경)
    report_design = f"""
    <div style="background-color: white; padding: 30px; border-radius: 15px; border: 2px solid #1e3a8a; color: #333;">
        <h2 style="color: #1e3a8a; margin-top: 0;">{report_month} 성과 보고서: {store_name}</h2>
        <p style="color: #666;">발행일: {datetime.now().strftime('%Y-%m-%d')}</p>
        <hr>
        
        <h3 style="color: #1e3a8a;">1. 네이버 플레이스 성과</h3>
        <p>📊 <b>상세페이지 클릭:</b> {curr_clicks:,}회 (전월 대비 {click_pct:+.1f}%)</p>
        <p>⭐ <b>신규 지도 리뷰:</b> {new_reviews}건 (누적 {curr_reviews}건)</p>
        
        <h3 style="color: #1e3a8a;">2. 인스타그램 성과</h3>
        <p>📱 <b>콘텐츠 노출:</b> {insta_views:,}회</p>
        <p>❤️ <b>고객 반응:</b> {insta_eng:,}건 (좋아요/댓글)</p>
        
        <h3 style="color: #1e3a8a;">3. 위드멤버 종합 진단</h3>
        <p>📝 <b>의견:</b> {special_note}</p>
    </div>
    """
    
    # [중요] 이 명령어가 디자인을 그려줍니다
    st.markdown(report_design, unsafe_allow_html=True)
    
    # 카톡용 텍스트 (따로 제공)
    st.divider()
    st.subheader("📱 카톡 전송용 요약")
    summary = f"[{store_name} {report_month} 성과]\n- 클릭: {curr_clicks}회\n- 신규리뷰: {new_reviews}건\n- 인스타: {insta_views}회\n위드멤버가 함께합니다."
    st.code(summary)

else:
    st.info("왼쪽 사이드바에 데이터를 입력한 후 버튼을 눌러주세요.")
