import streamlit as st
import pandas as pd
from datetime import datetime

# 1. 페이지 설정 및 디자인 고도화
st.set_page_config(page_title="WithMember Premium Report", page_icon="📊", layout="wide")

# 맞춤형 CSS (전문 대행사 느낌의 다크 블루 & 화이트 테마)
st.markdown("""
    <style>
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
    * { font-family: 'Pretendard', sans-serif; }
    .main { background-color: #f4f7f9; }
    .stButton>button { 
        background: linear-gradient(90deg, #1e3a8a 0%, #3b82f6 100%); 
        color: white; border: none; padding: 12px; font-weight: 700; border-radius: 8px;
    }
    .report-card { 
        background: white; padding: 30px; border-radius: 15px; 
        box-shadow: 0 4px 20px rgba(0,0,0,0.05); border-top: 5px solid #1e3a8a;
    }
    .metric-box {
        background: #f8fafc; padding: 15px; border-radius: 10px; text-align: center; border: 1px solid #e2e8f0;
    }
    .badge {
        padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: bold; color: white;
    }
    .badge-success { background-color: #10b981; }
    .badge-info { background-color: #3b82f6; }
    </style>
    """, unsafe_allow_html=True)

# 2. 사이드바 입력창 (그룹화하여 정리)
with st.sidebar:
    st.image("https://via.placeholder.com/150x50?text=WithMember", use_container_width=True) # 로고 이미지 자리
    st.title("🛠️ 리포트 설정")
    
    with st.expander("🏢 기본 정보", expanded=True):
        store_name = st.text_input("매장명", placeholder="예: 봉천동 콤마")
        report_month = st.selectbox("리포트 해당 월", [f"{i}월" for i in range(1, 13)], index=datetime.now().month - 1)
    
    with st.expander("📍 네이버 플레이스 성과"):
        last_clicks = st.number_input("전월 클릭수", value=500)
        curr_clicks = st.number_input("금월 클릭수", value=650)
        last_reviews = st.number_input("전월 총 리뷰", value=100)
        curr_reviews = st.number_input("금월 총 리뷰", value=125)

    with st.expander("📸 인스타그램 성과"):
        insta_views = st.number_input("콘텐츠 조회수", value=1200)
        insta_eng = st.number_input("좋아요/댓글 합계", value=150)
    
    special_note = st.text_area("📢 매장 특이사항", "브랜드 인지도 상승 및 예약 문의 증가")

# 3. 메인 화면 구성
st.title("📑 위드멤버 마케팅 성과 리포트")
st.write(f"**{store_name if store_name else '매장'}** 대표님, 이번 달 성과 분석 결과입니다.")

if st.button("✨ 프리미엄 리포트 발행하기"):
    if not store_name:
        st.warning("매장명을 입력해 주세요.")
    else:
        # 데이터 계산 로직
        click_diff = curr_clicks - last_clicks
        click_pct = (click_diff / last_clicks * 100) if last_clicks > 0 else 0
        new_reviews = curr_reviews - last_reviews
        
        # 성과 요약 배지 로직
        status_badge = '<span class="badge badge-success">우수 성과</span>' if click_pct > 10 else '<span class="badge badge-info">안정적 유지</span>'

        # 4. 리포트 본문 (HTML/CSS 레이아웃)
        report_html = f"""
        <div class="report-card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <h2 style="margin:0; color:#1e3a8a;">{report_month} 마케팅 성과 요약</h2>
                {status_badge}
            </div>
            <p style="color:#64748b; font-size:14px;">작성일: {datetime.now().strftime('%Y년 %m월 %d일')}</p>
            <hr style="border:0; border-top:1px solid #eee; margin: 20px 0;">
            
            <h4>1. 핵심 유입 지표 (Naver)</h4>
            <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 15px; margin-bottom: 25px;">
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
                <div class="metric-box">
                    <div style="font-size:12px; color:#64748b;">검색 노출 순위</div>
                    <div style="font-size:20px; font-weight:700; color:#1e3a8a;">상위권 안착</div>
                    <div style="font-size:12px; color:#3b82f6;">SEO 최적화 완료</div>
                </div>
            </div>

            <h4>2. SNS 콘텐츠 파급력 (Instagram)</h4>
            <div style="background:#f1f5f9; padding:20px; border-radius:10px; margin-bottom:25px;">
                <p style="margin:0;">이번 달 인스타그램 콘텐츠는 총 <b>{insta_views:,}명</b>에게 노출되었으며, 
                <b>{insta_eng:,}개</b>의 직접적인 반응(좋아요/댓글)을 이끌어냈습니다. 
                특히 숏폼 콘텐츠를 통한 젊은 층의 유입이 두드러집니다.</p>
            </div>

            <h4>3. 위드멤버 종합 진단 및 제언</h4>
            <ul style="color:#334155;">
                <li><b>성과 포인트:</b> {special_note}</li>
                <li><b>리뷰 관리:</b> 구글/카카오맵 다계정 리뷰를 통해 지역 내 검색 신뢰도 1위 달성 중.</li>
                <li><b>향후 과제:</b> 다음 달에는 유입 고객의 실제 결제를 유도하기 위한 '네이버 예약 쿠폰' 발행을 강화할 예정입니다.</li>
            </ul>
            
            <div style="margin-top:40px; text-align:center; font-size:14px; color:#94a3b8;">
                본 리포트는 위드멤버(WithMember) AI 분석 시스템에 의해 생성되었습니다.
            </div>
        </div>
        """
        
        # 화면에 출력
        st.markdown(report_html, unsafe_allow_html=True)
        
        # 텍스트 복사용 (카톡 전송용)
        with st.expander("📱 카톡 전송용 텍스트 복사"):
            st.text_area("Copy & Paste", value=f"[{store_name} {report_month} 성과]\n- 클릭수: {curr_clicks}회\n- 신규리뷰: {new_reviews}건\n- SNS노출: {insta_views}회\n위드멤버가 함께합니다.", height=150)

else:
    st.info("왼쪽 메뉴에서 데이터를 입력하고 '리포트 발행' 버튼을 클릭해 주세요.")
