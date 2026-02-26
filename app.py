import streamlit as st
import pandas as pd
from datetime import datetime

# 1. 페이지 설정
st.set_page_config(page_title="WithMember Marketing Report", page_icon="📈", layout="centered")

# 2. 사이드바 데이터 입력 (기존 항목 유지)
with st.sidebar:
    st.header("⚙️ 리포트 설정")
    store_name = st.text_input("매장명", value="봉천동 콤마")
    report_month = st.selectbox("리포트 월", [f"{i}월" for i in range(1, 13)], index=1)
    
    st.divider()
    with st.expander("📍 네이버 데이터", expanded=True):
        last_clicks = st.number_input("전월 클릭수", value=500)
        curr_clicks = st.number_input("금월 클릭수", value=652)
        last_reviews = st.number_input("전월 누적 리뷰", value=102)
        curr_reviews = st.number_input("금월 누적 리뷰", value=127)

    with st.expander("📸 인스타그램 데이터", expanded=True):
        insta_views = st.number_input("콘텐츠 노출수", value=1502)
        insta_eng = st.number_input("고객 반응수", value=152)
    
    special_note = st.text_area("📝 총평", "전체적인 지표가 안정적인 우상향 곡선을 그리고 있습니다.")

# 3. 메인 리포트 화면 (디자인)
st.title(f"🚀 {store_name} {report_month} 성과 리포트")
st.caption(f"발행일: {datetime.now().strftime('%Y-%m-%d')} | 위드멤버 마케팅 솔루션")

if st.button("✨ 리포트 발행하기"):
    # 데이터 계산
    click_diff = curr_clicks - last_clicks
    click_pct = (click_diff / last_clicks * 100) if last_clicks > 0 else 0
    new_reviews = curr_reviews - last_reviews

    # --- 섹션 1: 주요 수치 요약 ---
    st.subheader("📊 핵심 성과 요약")
    col1, col2, col3 = st.columns(3)
    col1.metric("플레이스 클릭", f"{curr_clicks:,}회", f"{click_pct:+.1f}%")
    col2.metric("신규 리뷰 등록", f"+{new_reviews}건", f"누적 {curr_reviews}건")
    col3.metric("인스타 도달", f"{insta_views:,}회", "상승세")

    st.divider()

    # --- 섹션 2: 시각적 그래프 ---
    st.subheader("📈 유입 성장 추이")
    chart_data = pd.DataFrame({
        "구분": ["지난달", "이번달"],
        "클릭수": [last_clicks, curr_clicks]
    })
    st.bar_chart(data=chart_data, x="구분", y="클릭수")

    # --- 섹션 3: 상세 분석 (코드 노출 없는 안전한 방식) ---
    st.subheader("🔍 위드멤버 종합 진단")
    
    with st.container(border=True):
        st.write(f"### 1. 네이버 로컬 SEO")
        st.write(f"이번 달 상세페이지 클릭수는 **{curr_clicks:,}회**로 전월 대비 **{abs(click_pct):.1f}%** 성장했습니다. 특히 **{new_reviews}건**의 신규 리뷰가 플랫폼 신뢰도를 높이고 있습니다.")
        
        st.write(f"### 2. 소셜 브랜드 지표")
        st.write(f"인스타그램 노출량 **{insta_views:,}회**를 기록하며 지역 내 브랜드 인지도가 확장되고 있습니다.")
        
        st.info(f"**💡 전문가 의견:**\n\n{special_note}")

    # --- 섹션 4: 카톡 전송용 ---
    st.divider()
    st.subheader("📱 카톡 전송용 텍스트")
    summary = f"[{store_name} {report_month} 성과]\n\n📈 클릭수: {curr_clicks}회 (▲{click_pct:.1f}%)\n⭐ 신규리뷰: {new_reviews}건\n📱 인스타: {insta_views}회\n\n위드멤버가 함께합니다! 🚀"
    st.code(summary, language="text")

else:
    st.info("왼쪽 사이드바에 데이터를 입력하고 버튼을 눌러주세요.")
