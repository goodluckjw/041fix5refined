import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from utils.xml_parser import parse_law_xml

st.title("부칙 개정 도우미")
st.write("법령 본문 중 검색어를 포함하는 조문을 찾아줍니다.")