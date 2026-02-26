import streamlit as st
import pandas as pd
from datetime import datetime

# 1. 페이지 설정 및 전문적인 디자인 테마 적용
st.set_page_config(page_title="WithMember Premium Marketing Report", page_icon="📈", layout="wide")

st.markdown("""
    <style>
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
    * { font-family: 'Pretendard', sans-serif; }
    .main-container { background-color: #f8fafc; padding: 40px; border-radius: 20px; }
    .stButton>button { 
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%); 
        color: white; border: none; padding: 15px; font-weight: 700; border-radius: 10px; box-shadow: 0 4px 15px rgba(59, 130, 246, 0.3);
    }
    .report-card { 
        background: white; padding: 40px; border-radius: 20px; 
        box-shadow: 0 10px 30px rgba(0,0,0,0.05); border: 1px solid #e2e8f0;
    }
    .metric-card {
        background: #ffffff; padding: 20px; border-radius: 12px; border: 1px solid #edf2f7;
        text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
    .section-title { color: #1e3a8a; border-left: 5px solid #1e3a8a; padding-left: 15px; margin: 30px 0 20px 0; }
    .highlight { color: #3b82f6; font-weight: 700; }
    </style>
    """, unsafe_allow_html=True)

# 2. 데이터 입력창 (사이드바)
with st.sidebar:
    st.image("https://via.placeholder.com/200x60.png?text=WithMember+Marketing", use_container_width=True)
    st.title("⚙️ 리포트 설정")
    store_name = st.text_input("매장명", value="봉천동 콤마")
    report_month = st.selectbox("리포트 월", [f"{i}월" for i in range(1, 13)], index=1)
    
    with st.expander("📍 네이버 데이터", expanded=True):
        last_clicks = st.number_input("지난달 클릭수", value=500)
        curr_clicks = st.number_input("이번달 클릭수", value=651)
        last_reviews = st.number_input("지난달 누적 리뷰", value=101)
        curr_reviews = st.number_input("이번달 누적 리뷰", value=126)

    with st.expander("📸 인스타그램 데이터", expanded=True):
        insta_views = st.number_input("콘텐츠 조회수", value=1501)
        insta_eng = st.number_input("고객 반응수", value=151)
    
    special_note = st.text_area("📝 종합 분석", "전체적인 브랜드 지표가 안정적인 우상향 곡선을 그리고 있습니다.")

# 3. 메인 리포트 생성 섹션
st.title("📈 위드멤버 통합 마케팅 성과 리포트")

if st.button("🚀 프리미엄 성과 리포트 발행"):
    # 데이터 계산 로직
    click_diff = curr_clicks - last_clicks
    click_pct = (click_diff / last_clicks * 100) if last_clicks > 0 else 0
    new_reviews = curr_reviews - last_reviews
    
    # ------------------ 리포트 상단 요약 카드 ------------------
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("네이버 플레이스 클릭", f"{curr_clicks:,}회", f"{click_pct:+.1f}%")
    with col2:
        st.metric("신규 리뷰 등록", f"+{new_reviews}건", f"누적 {curr_reviews}건")
    with col3:
        st.metric("인스타그램 확산", f"{insta_views:,}회", "상승세")

    # ------------------ 시각적 그래프 섹션 ------------------
    st.subheader("📊 유입 성장 추이")
    chart_data = pd.DataFrame({
        "구분": ["지난달", "이번달"],
        "유입량(클릭)": [last_clicks, curr_clicks]
    })
    st.bar_chart(data=chart_data, x="구분", y="유입량(클릭)", color="#1e3a8a")

    # ------------------ 상세 리포트 디자인 (HTML) ------------------
    report_html = f"""
    <div class="report-card">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <h1 style="color: #1e3a8a; margin: 0;">{report_month} 마케팅 성과 분석 리포트</h1>
            <div style="background: #e0f2fe; color: #0369a1; padding: 5px 15px; border-radius: 20px; font-weight: bold; font-size: 14px;">WithMember Official</div>
        </div>
        <p style="color: #64748b; margin-top: 5px;">대상 매장: <b>{store_name}</b> | 발행일: {datetime.now().strftime('%Y-%m-%d')}</p>
        
        <div class="section-title"><h3>1. 네이버 로컬 SEO 성과</h3></div>
        <p>네이버 플레이스 최적화를 통해 상세페이지 클릭수가 지난달 대비 <span class="highlight">{abs(click_pct):.1f}% 상승</span>했습니다. 
        특히 <span class="highlight">{new_reviews}건</span>의 고품질 신규 리뷰가 등록되며 잠재 고객의 방문 결정력이 대폭 강화되었습니다.</p>
        
        <div class="section-title"><h3>2. 인스타그램 소셜 임팩트</h3></div>
        <p>인스타그램 콘텐츠 노출량이 <span class="highlight">{insta_views:,}회</span>를 기록하며 지역 내 브랜드 인지도가 확장되었습니다. 
        단순 노출을 넘어 <span class="highlight">{insta_eng:,}건</span>의 고객 반응(좋아요/댓글)이 발생하여 매장에 대한 높은 관심을 확인했습니다.</p>
        
        <div class="section-title"><h3>3. 위드멤버 종합 진단 및 전략 제언</h3></div>
        <div style="background: #f8fafc; padding: 20px; border-radius: 12px; border-left: 4px solid #3b82f6;">
            <b>전문가 의견:</b> {special_note}<br><br>
            <b>차월 전략:</b> 현재의 높은 유입량을 바탕으로, 다음 달에는 실제 결제로 연결되는 '플레이스 쿠폰' 발행과 '숏폼 콘텐츠'를 집중 배포하여 매출 극대화를 노릴 계획입니다.
        </div>
        
        <div style="text-align: center; margin-top: 50px; color: #94a3b8; font-size: 13px;">
            본 리포트는 위드멤버 AI 마케팅 분석 솔루션을 통해 데이터 기반으로 작성되었습니다.
        </div>
    </div>
    """
    st.markdown(report_html, unsafe_allow_html=True)

    # ------------------ 카톡 복사용 ------------------
    st.divider()
    st.subheader("📱 카톡 전송용 텍스트")
    st.code(f"[{store_name} {report_month} 마케팅 리포트]\n\n✅ 플레이스 클릭: {curr_clicks}회 ({click_pct:+.1f}%)\n✅ 신규 리뷰: {new_reviews}건\n✅ SNS 노출: {insta_views}회\n\n위드멤버와 함께 매출 성장을 경험하세요! 🚀")

else:
    st.info("왼쪽 사이드바에 데이터를 입력하고 리포트 발행 버튼을 눌러주세요.")
