import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# Tela escolhida pelo endereço: ?p=kanban abre o kanban; sem parâmetro abre o painel
pagina = st.query_params.get("p", "")
kanban = pagina == "kanban"

st.set_page_config(
    page_title="Controle de tarefas" if kanban else "Time de Sourcing Aéreo",
    page_icon="✅" if kanban else "✈️",
    layout="wide",
)

# Esconde o cabeçalho/rodapé do Streamlit e tira as margens
st.markdown("""
<style>
  header, footer, #MainMenu {visibility: hidden;}
  .block-container {padding: 0 !important; max-width: 100% !important;}
  iframe {display: block; height: 100vh !important;}
</style>
""", unsafe_allow_html=True)

arquivo = "kanban.html" if kanban else "painel.html"
html = Path(__file__).parent.joinpath(arquivo).read_text(encoding="utf-8")
components.html(html, height=900, scrolling=True)
