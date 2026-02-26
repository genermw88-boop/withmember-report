import streamlit as st
import pandas as pd
from datetime import datetime

# 1. 페이지 설정 및 디자인 고도화
st.set_page_config(page_title="WithMember Marketing Report", page_icon="📈", layout="wide")

# 프리미엄 디자인 CSS 적용
st.markdown("""
    <style>
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
    * { font-family: 'Pretendard', sans-serif; }
    .main { background-color: #f0f2f6; }
    
    /* 버튼 디자인 */
    .stButton>button { 
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%); 
        color: white; border: none; padding: 18px; font-weight: 700; border-radius: 12px; 
        box-shadow: 0 4px 15px rgba(59, 130, 246, 0.4); width: 100%; transition: 0.3s;
    }
    
    /* 리포트 카드 디자인 */
    .report-container { 
        background: white; padding: 50px; border-radius: 30px; 
        box-shadow: 0 15px 50px rgba(0,0,0,0.08); border: 1px solid #e2e8f0;
        max-width: 900px; margin: auto;
    }
    
    /* 상단 헤더 */
    .header-box { border-bottom: 2px solid #1e3a8a; padding-bottom: 20px; margin-bottom: 30px; }
    .header-tag { background: #1e3a8a; color: white; padding: 4px 12px; border-radius: 6px; font-size: 12px; font-weight: 600; }
    
    /* 성과 요약 박스 */
    .summary-grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px; margin: 30px 0; }
    .summary-item { 
        background: #f8fafc; padding: 25px; border-radius: 20px; border: 1px solid #f1f5f9; text-align: center;
    }
    .summary-val { font-size: 28px; font-weight: 800; color: #1e3a8a; }
    .summary-label { font-size: 14px; color: #64748b; margin-top: 5px; }
    
    /* 섹션 타이틀 */
    .section-title { font-size: 20px; font-weight: 700; color: #1e3a8a; margin-top: 40px; margin-bottom: 15px; display: flex; align-items: center; }
    .section-title::before { content: ""; display: inline-block; width: 6px; height: 24px; background: #3b82f6; margin-right: 12px; border-radius: 3px; }
    
    /* 제언 박스 */
    .insight-box { background: #eff6ff; border-radius: 15px; padding: 25px; border-left: 6px solid #1e3a8a; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

# 2. 사이드바 데이터 입력창
with st.sidebar:
    st.title("⚙️ 리포트 대시보드")
    store_name = st.text_input("매장명", value="봉천동 콤마")
    report_month = st.selectbox("리포트 월", [f"{i}월" for i in range(1, 13)], index=datetime.now().month-1)
    
    with st.expander("📍 네이버 데이터", expanded=True):
        last_clicks = st.number_input("전월 클릭수", value=500)
        curr_clicks = st.number_input("금월 클릭수", value=652)
        last_reviews = st.number_input("전월 누적 리뷰", value=102)
        curr_reviews = st.number_input("금월 누적 리뷰", value=127)

    with st.expander("📸 인스타그램 데이터", expanded=True):
        insta_views = st.number_input("콘텐츠 노출수", value=1502)
        insta_eng = st.number_input("좋아요/댓글 반응", value=152)
    
    special_note = st.text_area("📝 총평 입력", "전체적인 브랜드 지표가 안정적인 우상향 곡선을 그리고 있으며, 지역 내 핵심 맛집 키워드 점유율이 상승했습니다.")

# 3. 메인 화면 구성
st.title("📊 WithMember Premium Marketing Report")

if st.button("🚀 위드멤버 프리미엄 리포트 발행"):
    # 데이터 계산
    click_diff = curr_clicks - last_clicks
    click_pct = (click_diff / last_clicks * 100) if last_clicks > 0 else 0
    new_reviews = curr_reviews - last_reviews
    
    # 리포트 본문 HTML 생성
    report_html = f"""
    <div class="report-container">
        <div class="header-box">
            <span class="header-tag">OFFICIAL REPORT</span>
            <h1 style="margin-top:10px; color:#1e3a8a;">{report_month} 마케팅 성과 분석 리포트</h1>
            <p style="color:#64748b;">대상 업체: <b>{store_name}</b> | 발행일: {datetime.now().strftime('%Y-%m-%d')}</p>
        </div>

        <div class="summary-grid">
            <div class="summary-item">
                <div class="summary-val">{curr_clicks:,}회</div>
                <div class="summary-label">플레이스 클릭 <span style="color:#10b981;">(▲{abs(click_pct):.1f}%)</span></div>
            </div>
            <div class="summary-item">
                <div class="summary-val">+{new_reviews}건</div>
                <div class="summary-label">신규 지도 리뷰 <span style="color:#3b82f6;">(누적 {curr_reviews}건)</span></div>
            </div>
            <div class="summary-item">
                <div class="summary-val">{insta_views:,}회</div>
                <div class="summary-label">인스타그램 도달수 <span style="color:#3b82f6;">(안정)</span></div>
            </div>
        </div>

        <div class="section-title">네이버 로컬 SEO 분석</div>
        <p style="color:#334155; line-height:1.7;">
            이번 달 네이버 플레이스 상세페이지 클릭수는 <b>{curr_clicks:,}회</b>를 기록하며 지난달 대비 <b>{abs(click_pct):.1f}%</b> 성장했습니다. 
            특히 <b>{new_reviews}건</b>의 실방문자 리뷰가 추가되어 플랫폼 내 신뢰도 점수가 크게 상승했으며, 이는 실제 예약 문의 증가로 이어지고 있습니다.
        </p>

        <div class="section-title">소셜 브랜드 인지도 지표</div>
        <p style="color:#334155; line-height:1.7;">
            인스타그램 콘텐츠 노출량은 총 <b>{insta_views:,}회</b>로 집계되었으며, 좋아요와 댓글을 포함한 고객 반응률은 전월 대비 안정적인 수치를 유지하고 있습니다. 
            숏폼 콘텐츠의 확산으로 신규 고객층의 유입 경로가 다각화되었습니다.
        </p>

        <div class="section-title">위드멤버 마케팅 총평 및 제언</div>
        <div class="insight-box">
            <p style="margin-top:0; font-weight:700; color:#1e3a8a;">🔍 마케팅 인사이트</p>
            <p style="color:#334155; margin-bottom:0;">{special_note}</p>
            <hr style="border:0; border-top:1px solid #d1e2ff; margin: 15px 0;">
            <p style="margin-top:0; font-size:14px; color:#1e3a8a;"><b>💡 다음 달 핵심 과제:</b> 확보된 높은 유입량을 매출로 전환하기 위해 플레이스 한정 쿠폰 발행 및 메뉴 사진 최적화를 진행할 예정입니다.</p>
        </div>

        <div style="text-align: center; margin-top: 60px; color: #cbd5e1; font-size: 13px; font-weight:500;">
            본 리포트는 위드멤버(WithMember) AI 분석 시스템에 의해 발행되었습니다.
        </div>
    </div>
    """
    
    # 화면 출력
    st.markdown(report_html, unsafe_allow_html=True)
    
    # 카톡 전송용 요약 (깔끔하게 코드박스로 제공)
    st.divider()
    st.subheader("📱 카톡 전송용 요약본")
    st.code(f"[{store_name} {report_month} 성과]\n\n📈 클릭수: {curr_clicks}회 (▲{click_pct:.1f}%)\n⭐ 신규리뷰: {new_reviews}건\n📱 인스타: {insta_views}회\n\n위드멤버와 함께 성공적인 성장을 만들어가세요! 🚀")

else:
    st.info("왼쪽 사이드바에 데이터를 입력하고 버튼을 눌러주세요.")
