import streamlit as st
from deep_translator import GoogleTranslator

# 웹 페이지 기본 설정
st.set_page_config(page_title="다국어 번역기", page_icon="🌐", layout="wide")

st.title("🌐 한국어 다국어 번역기")
st.write("한국어를 입력하면 영어, 중국어(간체), 일본어로 동시에 번역해 줍니다.")

# 언어 코드 설정
languages = {
    "영어": "en",
    "중국어(간체)": "zh-CN",
    "일본어": "ja"
}

# 텍스트 입력창
text_to_translate = st.text_area("번역할 한국어 텍스트를 입력하세요:", height=150, placeholder="여기에 텍스트를 입력하세요...")

# 번역 버튼
if st.button("번역하기", type="primary"):
    if text_to_translate.strip():
        st.divider()
        st.subheader("✨ 번역 결과")
        
        # 화면을 3개의 열로 나누기
        col1, col2, col3 = st.columns(3)
        
        # 영어 번역
        with col1:
            st.markdown("### 🇺🇸 영어")
            try:
                translated_en = GoogleTranslator(source='ko', target=languages['영어']).translate(text_to_translate)
                st.info(translated_en)
            except Exception as e:
                st.error("번역 중 오류가 발생했습니다.")
                
        # 중국어 번역
        with col2:
            st.markdown("### 🇨🇳 중국어")
            try:
                translated_zh = GoogleTranslator(source='ko', target=languages['중국어(간체)']).translate(text_to_translate)
                st.success(translated_zh)
            except Exception as e:
                st.error("번역 중 오류가 발생했습니다.")
                
        # 일본어 번역
        with col3:
            st.markdown("### 🇯🇵 일본어")
            try:
                translated_ja = GoogleTranslator(source='ko', target=languages['일본어']).translate(text_to_translate)
                st.warning(translated_ja)
            except Exception as e:
                st.error("번역 중 오류가 발생했습니다.")
    else:
        st.error("번역할 텍스트를 먼저 입력해 주세요!")
