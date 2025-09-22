from templates.manterclienteUI import ManterClienteUI
from templates.manterServicoUI import ManterServicoUI
import streamlit as st

class IndexUI:
    def main():
        st.sidebar.title("Sistema de Agendamento")
        opcao = st.sidebar.selectbox("Escolha uma opção", ["Clientes", "Serviços"])

        if opcao == "Clientes":
            ManterClienteUI.main()
        elif opcao == "Serviços":
            ManterServicoUI.main()

IndexUI.main()