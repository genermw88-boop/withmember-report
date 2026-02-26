import streamlit as st
import pandas as pd
from datetime import datetime

# 1. 페이지 설정 및 디자인
st.set_page_config(page_title="위드멤버 AI 리포트 생성기", page_icon="🚀")

# 스타일 설정 (위드멤버 브랜드 느낌)
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { width: 100%; border-radius: 5px; background-color: #007bff; color: white; }
    .report-box { padding: 20px; border: 1px solid #ddd; border-radius: 10px; background-color: white; line-height: 1.6; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 위드멤버(WithMember) AI 성과 리포트")
st.subheader("소상공인 대표님을 위한 맞춤형 월간 보고서 생성기")

# 2. 사이드바 - 기본 정보 입력
with st.sidebar:
    st.header("📋 매장 정보 입력")
    store_name = st.text_input("매장명", placeholder="예: 봉천동 콤마")
    report_month = st.selectbox("리포트 해당 월", [f"{i}월" for i in range(1, 13)], index=datetime.now().month - 1)
    
    st.divider()
    
    st.header("📊 수치 데이터")
    last_clicks = st.number_input("지난달 클릭수 (네이버)", min_value=0, value=500)
    curr_clicks = st.number_input("이번달 클릭수 (네이버)", min_value=0, value=650)
    review_count = st.number_input("신규 리뷰 등록 합계 (구글/카카오)", min_value=0, value=20)
    
    st.divider()
    
    st.header("✍️ 추가 메모")
    special_note = st.text_area("특이사항", placeholder="예: 주말 예약 문의가 눈에 띄게 늘었음")

# 3. 리포트 생성 로직
if st.button("✨ 전문 리포트 생성하기"):
    if not store_name:
        st.error("매장명을 입력해주세요!")
    else:
        # 데이터 계산
        growth = ((curr_clicks - last_clicks) / last_clicks * 100) if last_clicks > 0 else 0
        growth_mark = "▲" if growth >= 0 else "▼"
        
        # 리포트 텍스트 조립
        report_content = f"""
### **[위드멤버] {report_month} 마케팅 성과 보고서: {store_name}**

---

#### **1. 종합 성과 요약 🚀**
이번 {report_month}은 위드멤버의 집중 관리를 통해 전체 유입량이 **지난달 대비 {growth_mark}{abs(growth):.1f}%** 변화하는 성과를 거두었습니다. 특히 지도 검색 기반의 유입이 안정화되며 매장 인지도가 크게 상승했습니다.

#### **2. 채널별 노출 및 유입 현황 📊**
* **네이버 플레이스:** 클릭수 **{curr_clicks:,}회** 달성 (전월 {last_clicks:,}회 대비 {growth_mark}{abs(growth):.1f}%)
* **신규 리뷰 관리:** 구글 맵 & 카카오맵 **총 {review_count}건** 등록 완료
    - 실제 방문자 컨셉의 정성스러운 리뷰를 통해 플랫폼 내 신뢰도 점수를 확보했습니다.

#### **3. 마케팅 성과 포인트 ✨**
* **리뷰 평점 최적화:** 다계정 리뷰 작업을 통해 검색 시 상위 노출 환경을 조성하였으며, 잠재 고객들에게 '믿고 방문할 만한 매장'이라는 긍정적인 첫인상을 심어주었습니다.
* **특이사항:** {special_note if special_note else "전체적인 브랜드 지표가 우상향 중입니다."}

#### **4. 다음 달 전략 제언 (AI 컨설팅) 💡**
현재 유입량이 안정 궤도에 올랐으므로, 다음 달에는 **'재방문 유도'**를 위한 플레이스 쿠폰 발행 및 **'숏폼 영상'** 배포를 병행하여 매출 극대화를 노려볼 것을 제안드립니다.

---
**작성일:** {datetime.now().strftime('%Y-%m-%d')} | **담당:** 위드멤버 마케팅팀
        """
        
        # 결과 출력
        st.success("리포트가 성공적으로 생성되었습니다!")
        st.markdown(f'<div class="report-box">{report_content}</div>', unsafe_allow_html=True)
        
        # 복사 기능 제공
        st.text_area("아래 텍스트를 복사해서 카톡이나 이메일로 보내세요:", value=report_content, height=300)

else:
    st.info("왼쪽 사이드바에 데이터를 입력하고 버튼을 눌러주세요.")