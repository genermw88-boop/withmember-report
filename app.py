import streamlit as st
import pandas as pd
from datetime import datetime

# 1. 페이지 설정
st.set_page_config(page_title="WithMember AI Analysis Report", page_icon="📝", layout="centered")

# 디자인 테마 (전문 보고서 느낌)
st.markdown("""
    <style>
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
    * { font-family: 'Pretendard', sans-serif; }
    .stButton>button { 
        background-color: #1e3a8a; color: white; border-radius: 8px; width: 100%; height: 50px; font-weight: bold;
    }
    .report-frame {
        border: 1px solid #e2e8f0; padding: 40px; border-radius: 5px; background-color: white; color: #1e293b;
    }
    .main-title { font-size: 26px; font-weight: 800; color: #1e3a8a; border-bottom: 2px solid #1e3a8a; padding-bottom: 10px; margin-bottom: 20px; }
    .sub-title { font-size: 18px; font-weight: 700; color: #334155; margin-top: 25px; margin-bottom: 10px; }
    .content-text { line-height: 1.8; color: #475569; font-size: 15px; }
    .highlight { color: #2563eb; font-weight: 700; }
    </style>
    """, unsafe_allow_html=True)

# 2. 사이드바 데이터 입력창
with st.sidebar:
    st.header("⚙️ 데이터 입력")
    store_name = st.text_input("매장명", value="봉천동 콤마")
    report_month = st.selectbox("리포트 월", [f"{i}월" for i in range(1, 13)], index=1)
    
    st.divider()
    st.subheader("📍 네이버 통계")
    last_clicks = st.number_input("전월 클릭수", value=500)
    curr_clicks = st.number_input("금월 클릭수", value=650)
    last_reviews = st.number_input("전월 누적 리뷰", value=100)
    curr_reviews = st.number_input("금월 누적 리뷰", value=125)

    st.subheader("📸 인스타그램 통계")
    insta_views = st.number_input("조회수(노출)", value=1500)
    insta_eng = st.number_input("반응(좋아요/댓글)", value=150)

# 3. 리포트 발행 로직
st.title("📂 위드멤버 마케팅 보고서 시스템")

if st.button("📄 AI 분석 보고서 발행하기"):
    # 데이터 계산 및 AI 판단 로직
    click_pct = ((curr_clicks - last_clicks) / last_clicks * 100) if last_clicks > 0 else 0
    new_reviews = curr_reviews - last_reviews
    
    # 성과 등급 판단
    score = 0
    if click_pct > 10: score += 1
    if new_reviews >= 10: score += 1
    if insta_views > 1000: score += 1
    
    status = "매우 우수" if score >= 3 else "안정적 성장"
    
    # 보고서 텍스트 구성 (AI가 판단하여 서술하는 형식)
    report_content = f"""
    <div class="report-frame">
        <div class="main-title">{report_month} 마케팅 성과 정기 보고서</div>
        <p style="text-align: right; color: #94a3b8; font-size: 13px;">발행번호: WM-{datetime.now().strftime('%Y%m%d')}-01</p>
        
        <p class="content-text">
            <b>수신:</b> {store_name} 대표님 귀하<br>
            <b>발신:</b> 위드멤버(WithMember) 마케팅 분석팀
        </p>

        <div class="sub_title">1. 종합 분석 요약</div>
        <p class="content-text">
            본 매장의 {report_month} 마케팅 운영 결과, 전월 대비 전체적인 브랜드 지표가 <span class="highlight">{status}</span>한 상태로 진단되었습니다. 
            특히 검색 노출 기반의 유입량과 고객 신뢰도를 상징하는 리뷰 지표의 동반 상승은 지역 내 핵심 상권에서의 경쟁력이 강화되고 있음을 시사합니다.
        </p>

        <div class="sub-title">2. 로컬 SEO(네이버 플레이스) 성과 분석</div>
        <p class="content-text">
            플레이스 상세페이지 클릭수는 금월 총 <span class="highlight">{curr_clicks:,}회</span>를 기록하였습니다. 
            이는 전월 대비 <span class="highlight">{abs(click_pct):.1f}% 상승</span>한 수치로, 잠재 고객의 검색 키워드와 매장의 매칭 효율이 최적화되었음을 의미합니다. 
            또한, <span class="highlight">{new_reviews}건</span>의 신규 리뷰가 추가되어 플랫폼 내 '방문자 평판' 점수가 개선되었으며, 이는 검색 결과 상단 노출 유지의 핵심 동력으로 작용할 것입니다.
        </p>

        <div class="sub-title">3. SNS 콘텐츠 파급력 평가</div>
        <p class="content-text">
            인스타그램 기반의 홍보 활동 결과, 콘텐츠 노출수 <span class="highlight">{insta_views:,}회</span> 및 고객 반응 <span class="highlight">{insta_eng:,}건</span>을 달성하였습니다. 
            단순 노출을 넘어 고객들이 직접 참여하는 인터랙션 수치가 안정적으로 유지되고 있어, 브랜드에 대한 호감도가 충성 고객층으로 전이되는 긍정적인 단계에 진입한 것으로 판단됩니다.
        </p>

        <div class="sub-title">4. 마케팅 전략 제언</div>
        <p class="content-text" style="background-color: #f1f5f9; padding: 20px; border-radius: 10px;">
            <b>[AI 전략 진단]:</b> 현재 유입 데이터는 충분히 확보되었으나, 실제 방문 확정률을 높이기 위한 '트리거'가 필요한 시점입니다. 
            다음 달에는 <b>플레이스 쿠폰 활용</b> 및 <b>숏폼 영상의 지역 타겟팅</b>을 강화하여 유입 고객의 실제 매장 방문 전환율을 15% 이상 끌어올리는 것을 목표로 설정할 것을 권장합니다.
        </p>

        <div style="margin-top: 50px; text-align: center; border-top: 1px solid #eee; padding-top: 20px;">
            <p style="color: #1e3a8a; font-weight: 800; font-size: 18px;">WithMember</p>
            <p style="color: #94a3b8; font-size: 12px;">성공적인 비즈니스 파트너, 위드멤버가 늘 함께하겠습니다.</p>
        </div>
    </div>
    """
    
    # 화면에 출력
    st.markdown(report_content, unsafe_allow_html=True)
    
    # 카톡용 텍스트
    st.divider()
    with st.expander("📱 카톡 전송용 요약본"):
        summary = f"[{store_name} {report_month} 성과 요약]\n\n✅ 플레이스 유입: {curr_clicks}회 (▲{click_pct:.1f}%)\n✅ 신규 리뷰: {new_reviews}건\n✅ SNS 노출: {insta_views}회\n\nAI 분석 결과 '{status}' 등급으로 진단되었습니다. 상세 보고서는 위드멤버 리포트에서 확인하세요! 🚀"
        st.code(summary, language="text")

else:
    st.info("왼쪽에서 매장 데이터를 입력한 후 버튼을 눌러주세요.")
