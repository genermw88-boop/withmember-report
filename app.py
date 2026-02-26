import streamlit as st
import pandas as pd
from datetime import datetime

# 1. 페이지 설정 및 디자인 고도화
st.set_page_config(page_title="WithMember Premium Report", page_icon="📊", layout="wide")

# CSS 스타일 정의
st.markdown("""
    <style>
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
    * { font-family: 'Pretendard', sans-serif; }
    .main { background-color: #f4f7f9; }
    .stButton>button { 
        background: linear-gradient(90deg, #1e3a8a 0%, #3b82f6 100%); 
        color: white; border: none; padding: 12px; font-weight: 700; border-radius: 8px;
        width: 100%;
    }
    .report-card { 
        background: white; padding: 30px; border-radius: 15px; 
        box-shadow: 0 4px 20px rgba(0,0,0,0.05); border-top: 5px solid #1e3a8a;
        color: #334155;
    }
    .metric-container {
        display: flex; gap: 15px; margin-bottom: 25px; justify-content: space-between;
    }
    .metric-box {
        flex: 1; background: #f8fafc; padding: 15px; border-radius: 10px; 
        text-align: center; border: 1px solid #e2e8f0;
    }
    .badge {
        padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: bold; color: white;
    }
    .badge-success { background-color: #10b981; }
    </style>
    """, unsafe_allow_html=True)

# 2. 사이드바 설정
with st.sidebar:
    st.title("🛠️ 리포트 설정")
    store_name = st.text_input("매장명", placeholder="예: 봉천동 콤마")
    report_month = st.selectbox("리포트 해당 월", [f"{i}월" for i in range(1, 13)], index=datetime.now().month - 1)
    
    st.divider()
    st.subheader("📍 네이버 성과")
    last_clicks = st.number_input("전월 클릭수", value=500)
    curr_clicks = st.number_input("금월 클릭수", value=650)
    last_reviews = st.number_input("전월 총 리뷰", value=100)
    curr_reviews = st.number_input("금월 총 리뷰", value=125)

    st.subheader("📸 인스타그램 성과")
    insta_views = st.number_input("콘텐츠 조회수", value=1200)
    insta_eng = st.number_input("좋아요/댓글 합계", value=150)
    
    special_note = st.text_area("📢 특이사항", "브랜드 인지도 상승 및 예약 문의 증가")

# 3. 메인 화면
st.title("📑 위드멤버 마케팅 성과 리포트")

if st.button("✨ 프리미엄 리포트 발행하기"):
    if not store_name:
        st.warning("매장명을 입력해 주세요.")
    else:
        # 데이터 계산
        click_diff = curr_clicks - last_clicks
        click_pct = (click_diff / last_clicks * 100) if last_clicks > 0 else 0
        new_reviews = curr_reviews - last_reviews
        
        # HTML 리포트 생성
        report_html = f"""
        <div class="report-card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <h2 style="margin:0; color:#1e3a8a;">{report_month} 성과 보고서: {store_name}</h2>
                <span class="badge badge-success">우수 성과</span>
            </div>
            <p style="color:#64748b; font-size:14px;">발행일: {datetime.now().strftime('%Y-%m-%d')}</p>
            <hr style="border:0; border-top:1px solid #eee; margin: 20px 0;">
            
            <h4 style="color:#1e3a8a;">1. 네이버 플레이스 유입 지표</h4>
            <div class="metric-container">
                <div class="metric-box">
                    <div style="font-size:12px; color:#64748b;">플레이스 클릭</div>
                    <div style="font-size:20px; font-weight:700; color:#1e3a8a;">{curr_clicks:,}회</div>
                    <div style="font-size:12px; color:#10b981;">전월 대비 ▲{abs(click_pct):.1f}%</div>
                </div>
                <div class="metric-box">
                    <div style="font-size:12px; color:#64748b;">신규 지도 리뷰</div>
                    <div style="font-size:20px; font-weight:700; color:#1e3a8a;">+{new_reviews}건</div>
                    <div style="font-size:12px; color:#3b82f6;">누적 {curr_reviews:,}건</div>
                </div>
            </div>

            <h4 style="color:#1e3a8a;">2. SNS 콘텐츠 파급력</h4>
            <div style="background:#f1f5f9; padding:20px; border-radius:10px; margin-bottom:25px;">
                인스타그램 콘텐츠는 이번 달 총 <b>{insta_views:,}회</b> 노출되었으며, 
                <b>{insta_eng:,}개</b>의 유의미한 고객 반응을 이끌어냈습니다.
            </div>

            <h4 style="color:#1e3a8a;">3. 위드멤버 종합 진단</h4>
            <p><b>성과 포인트:</b> {special_note}</p>
            <p style="font-size:14px; color:#64748b;">본 리포트는 위드멤버 마케팅 분석 시스템을 통해 정식 발행되었습니다.</p>
        </div>
        """
        
        # 리포트 출력 (이 부분이 핵심입니다)
        st.markdown(report_html, unsafe_allow_html=True)
        
        # 카톡 복사용 텍스트
        st.divider()
        st.subheader("📱 모바일 전송용 요약")
        summary_text = f"[{store_name} {report_month} 성과]\n- 클릭수: {curr_clicks}회\n- 신규리뷰: {new_reviews}건\n- SNS노출: {insta_views}회\n위드멤버가 함께합니다."
        st.code(summary_text)

else:
    st.info("왼쪽에서 데이터를 입력하고 버튼을 눌러주세요.")
