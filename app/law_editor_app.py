import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from utils.xml_parser import parse_law_xml

st.title("부칙 개정 도우미")
st.write("법령 본문 중 검색어를 포함하는 조문을 찾아줍니다.")

search_word = st.text_input("🔍 찾을 단어", placeholder="예: 건조물")

if st.button("법률 검색"):
    st.write(f"🔎 '{search_word}'을(를) 포함하는 조문을 검색 중입니다...")
    
    # 예시 XML 파일 경로 (테스트용)
    file_path = "./data/GYEONGBUM.xml"
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            xml_content = f.read()
        results = parse_law_xml(xml_content, search_word)
        if results:
            for res in results:
                st.markdown(res, unsafe_allow_html=True)
        else:
            st.warning("해당 검색어를 포함한 조문이 없습니다.")
    except Exception as e:
        st.error(f"⚠️ 파일 로드 중 오류 발생: {e}")
