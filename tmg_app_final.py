import streamlit as st
from pathlib import Path
from PIL import Image

# ==========================================
# CONFIGURAÇÃO DA PÁGINA
# ==========================================
st.set_page_config(
    page_title="TMG Sistema de Análise",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# ESTILO CSS PERSONALIZADO (DARK SAAS 3D)
# ==========================================
st.markdown("""
<style>
    .stApp {
        background-color: #121212;
        color: #e0e0e0;
    }

    .main-header {
        text-align: center;
        color: #FFFFFF;
        padding: 20px;
        font-family: 'Segoe UI', sans-serif;
        font-weight: 800;
        letter-spacing: 2px;
        border-bottom: 2px solid #333;
        margin-bottom: 30px;
    }

    [data-testid="stSidebar"] {
        background-color: #1a1a1a;
        border-right: 1px solid #333;
        padding-top: 20px;
    }

    div.stButton > button {
        width: 100%;
        border-radius: 10px;
        border: none;
        padding: 15px 20px;
        background: linear-gradient(145deg, #222, #111);
        color: #ccc;
        font-weight: 600;
        box-shadow: 3px 3px 6px #0a0a0a, -1px -1px 6px #2a2a2a;
        transition: 0.3s;
        margin-bottom: 10px;
        text-align: left;
    }

    div.stButton > button:hover {
        color: #ff8c00;
        border: 1px solid #ff8c00;
        transform: translateY(-2px);
    }

    .stButton > button[kind="primary"] {
        background: linear-gradient(145deg, #ff9e33, #e67600) !important;
        color: white !important;
        box-shadow: 4px 4px 10px #0a0a0a !important;
    }

    .card {
        background-color: #1e1e1e;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #333;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# ESTADO
# ==========================================
if 'pagina_ativa' not in st.session_state:
    st.session_state.pagina_ativa = 'Checklist'

if 'logo_sistema' not in st.session_state:
    st.session_state.logo_sistema = None

def ir_para(pagina):
    st.session_state.pagina_ativa = pagina

# ==========================================
# SIDEBAR
# ==========================================
with st.sidebar:

    # MENU 3D
    st.markdown("""
    <h2 style='
        text-align: center;
        color: #ff8c00;
        font-weight: 900;
        letter-spacing: 2px;
        text-shadow: 
            2px 2px 0 #000,
            4px 4px 6px rgba(0,0,0,0.8);
    '>MENU</h2>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # BOTÕES
    if st.button("📋 Checklist", key="btn_check"):
        ir_para('Checklist')

    if st.button("📊 Marcador de Grid", key="btn_grid"):
        ir_para('Grid')

    if st.button("📤 Upload de Imagens", key="btn_upload"):
        ir_para('Upload')

    if st.button("⚙️ Configurações", key="btn_config"):
        ir_para('Config')

    if st.button("🗂️ Bases", key="btn_bases"):
        ir_para('Bases')

    st.markdown("---")
    st.caption("TMG v2.0 - 2026")

# ==========================================
# TOPO (LOGO)
# ==========================================
if st.session_state.logo_sistema:
    col1, col2, col3 = st.columns([1,1,1])
    with col2:
        st.image(st.session_state.logo_sistema, use_column_width=True)

st.markdown("<h1 class='main-header'>TMG SISTEMA DE ANÁLISE</h1>", unsafe_allow_html=True)

# ==========================================
# CONTEÚDO
# ==========================================
main_container = st.container()

with main_container:

    # CHECKLIST
    if st.session_state.pagina_ativa == 'Checklist':
        st.subheader("📋 Controle de Validação")

        col1, col2 = st.columns(2)

        with col1:
            st.checkbox("Verificação de Ortofotos")
            st.checkbox("Calibração de Sensores")
            st.checkbox("Sincronização de Banco de Dados")

        with col2:
            st.checkbox("Revisão de Metadados")
            st.checkbox("Relatório de Tassel (Pendão)")

    # GRID
    elif st.session_state.pagina_ativa == 'Grid':
        st.subheader("📊 Organização em Grade e Métricas")

        cols = st.columns(3)

        for i in range(3):
            with cols[i]:
                st.markdown(f"""
                <div class='card'>
                    <h3 style='color: #ff8c00;'>Grid {i+1}</h3>
                    <p>Status: Operacional</p>
                    <p style='font-size: 24px; font-weight: bold;'>85%</p>
                </div>
                """, unsafe_allow_html=True)

    # UPLOAD
    elif st.session_state.pagina_ativa == 'Upload':
        st.subheader("📤 Central de Arquivos")

        st.info("Arraste e solte as imagens do experimento agrícola abaixo.")

        uploaded_files = st.file_uploader(
            "Imagens (PNG, JPG)",
            type=["png", "jpg"],
            accept_multiple_files=True
        )

        if uploaded_files:
            st.success(f"{len(uploaded_files)} arquivos prontos para processamento.")

            if st.button("Iniciar Processamento", type="primary"):
                st.toast("Iniciando análise por IA...")

    # CONFIG
    elif st.session_state.pagina_ativa == 'Config':
        st.subheader("⚙️ Painel Administrativo")

        with st.expander("Identidade Visual", expanded=True):
            st.write("Atualize a logo do sistema:")

            nova_logo = st.file_uploader(
                "Escolha uma nova logo",
                type=["png", "jpg", "jpeg"]
            )

            if nova_logo:
                st.session_state.logo_sistema = Image.open(nova_logo)
                st.success("Logo atualizada!")

        with st.expander("Caminhos de Diretório"):
            st.text_input("Diretório de Banco de Dados", value="/mnt/storage/tmg_data")

            st.button("Salvar Configurações", type="primary")

    # BASES (NOVA)
    elif st.session_state.pagina_ativa == 'Bases':
        st.subheader("🗂️ Gestão de Bases de Dados")

        st.info("Área destinada ao gerenciamento de bases do sistema.")

        col1, col2 = st.columns(2)

        with col1:
            st.text_input("Nome da Base")
            st.text_input("Caminho da Base")

        with col2:
            st.selectbox("Tipo de Base", ["Local", "Nuvem", "API"])
            st.button("Conectar Base", type="primary")

# ==========================================
# FOOTER
# ==========================================
st.markdown("<br><br>", unsafe_allow_html=True)
st.divider()

st.markdown(
    "<p style='text-align: center; color: #555;'>Estrutura Modular Profissional | Python 3.12</p>",
    unsafe_allow_html=True
)
