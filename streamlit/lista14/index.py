from templates.manterclienteUI import ManterClienteUI
from templates.manterServicoUI import ManterServicoUI
from templates.manterhorarioUI import ManterHorarioUI
from templates.manterprofissionalUI import ManterProfissionalUI
from templates.alterarsenhaUI import AlterarSenhaUI
import streamlit as st
from templates.abrircontaUI import AbrirContaUI
from templates.loginUI import LoginUI
from templates.loginUI_P import LoginUI_P
from templates.perfilclienteUI import PerfilClienteUI
from templates.perfilprofissionalUI import PerfilProfissionalUI
from templates.agendarservicoUI import AgendarServicoUI
from templates.gerenciaragenda import GerenciarAgendaUI
from templates.meusservicosUI import MeusServicosUI
from templates.confirmarservicoUI import ConfirmarServicoUI
from templates.chatUI import ChatUI
from templates.chatUI_P import ChatUI_P
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
        op = st.sidebar.selectbox("Menu", ["Meus Dados", "Agendar Serviço", "Meus Serviços", "Chat"])
        if op == "Meus Dados": PerfilClienteUI.main()
        if op == "Agendar Serviço": AgendarServicoUI.main()
        if op == "Meus Serviços": MeusServicosUI.main()
        if op == "Chat": ChatUI.main()
    def menu_profissional():
        op = st.sidebar.selectbox("Menu", ["Meus Dados", "gerenciar agenda","confirmar serviço", "Chat"])
        if op == "Meus Dados": PerfilProfissionalUI.main()
        if op == "gerenciar agenda": GerenciarAgendaUI.main()
        if op == "confirmar serviço": ConfirmarServicoUI.main()
        if op == "Chat": ChatUI_P.main()
    def menu_admin(): 
        op = st.sidebar.selectbox("Menu", ["Cadastro de Clientes", 
                                            "Cadastro de Serviços", 
                                            "Cadastro de Horários", 
                                            "Cadastro de Profissionais",
                                            "Alterar Senha"])
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Serviços": ManterServicoUI.main()
        if op == "Cadastro de Horários": ManterHorarioUI.main()
        if op == "Cadastro de Profissionais": ManterProfissionalUI.main()
        if op == "Alterar Senha": AlterarSenhaUI.main()
    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            keys = ["cliente_id", "cliente_nome", "profissional_id", "profissional_nome"]
            for key in keys:
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()  # versão nova do Streamlit
    def sidebar():
        cliente_logado = "cliente_id" in st.session_state
        profissional_logado = "profissional_id" in st.session_state
        admin = cliente_logado and st.session_state["cliente_nome"] == "admin"

        if not cliente_logado and not profissional_logado:
            IndexUI.menu_visitante()
        else:
            if admin:
                st.sidebar.write(f"Bem-vindo(a), {st.session_state['cliente_nome']} (Admin)")
                IndexUI.menu_admin()
            elif profissional_logado:
                st.sidebar.write(f"Bem-vindo(a), {st.session_state['profissional_nome']}")
                IndexUI.menu_profissional()
            else:
                st.sidebar.write(f"Bem-vindo(a), {st.session_state['cliente_nome']}")
                IndexUI.menu_cliente()

            IndexUI.sair_do_sistema()


IndexUI.main()