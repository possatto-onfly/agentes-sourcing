import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="Time de Sourcing Aéreo", page_icon="✈️", layout="wide")

# Esconde o cabeçalho/rodapé do Streamlit e tira as margens
st.markdown("""
<style>
  header, footer, #MainMenu {visibility: hidden;}
  .block-container {padding: 0 !important; max-width: 100% !important;}
  iframe {display: block;}
</style>
""", unsafe_allow_html=True)

html = Path(__file__).parent.joinpath("painel.html").read_text(encoding="utf-8")
components.html(html, height=900, scrolling=True)
