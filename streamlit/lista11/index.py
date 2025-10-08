from templates.manterclienteUI import ManterClienteUI
from templates.manterServicoUI import ManterServicoUI
from templates.manterhorarioUI import ManterHorarioUI
from templates.manterprofissionalUI import ManterProfissionalUI
import streamlit as st
from templates.abrircontaUI import AbrirContaUI
from templates.loginUI import LoginUI
from templates.loginUI_P import LoginUI_P
from templates.perfilclienteUI import PerfilClienteUI
from templates.perfilprofissionalUI import PerfilProfissionalUI
from views import View

class IndexUI:
    def main():
        View.cliente_criar_admin()
        IndexUI.sidebar()
    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Entrar no Sistema de profissionais", "Abrir Conta"])
        if op == "Entrar no Sistema": LoginUI.main()
        if op == "Entrar no Sistema de profissionais": LoginUI_P.main()
        if op == "Abrir Conta": AbrirContaUI.main()
    def menu_cliente():
        op = st.sidebar.selectbox("Menu", ["Meus Dados"])
        if op == "Meus Dados": PerfilClienteUI.main()
    def menu_profissional():
        op = st.sidebar.selectbox("Menu", ["Meus Dados"])
        if op == "Meus Dados": PerfilProfissionalUI.main()
    def menu_admin(): 
        op = st.sidebar.selectbox("Menu", ["Cadastro de Clientes", 
                                            "Cadastro de Serviços", 
                                            "Cadastro de Horários", 
                                            "Cadastro de Profissionais"])
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Serviços": ManterServicoUI.main()
        if op == "Cadastro de Horários": ManterHorarioUI.main()
        if op == "Cadastro de Profissionais": ManterProfissionalUI.main()
    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["usuario_id"]
            del st.session_state["usuario_nome"]
            st.rerun()
    def sidebar():
        if "usuario_id" not in st.session_state:
            IndexUI.menu_visitante() 
        else:
            admin = st.session_state["usuario_nome"] == "admin"
            profissional = not admin and View.profissional_listar_id(st.session_state["usuario_id"]) is not None
            st.sidebar.write("Bem-vindo(a), " + st.session_state["usuario_nome"])
            if admin: IndexUI.menu_admin()
            elif profissional: IndexUI.menu_profissional()
            else: IndexUI.menu_cliente()
            IndexUI.sair_do_sistema()


IndexUI.main()