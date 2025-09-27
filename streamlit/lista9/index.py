from templates.manterclienteUI import ManterClienteUI
from templates.manterServicoUI import ManterServicoUI
from templates.manterhorarioUI import ManterHorarioUI
from templates.manterprofissionalUI import ManterProfissionalUI
import streamlit as st

class IndexUI:
    def main():
        st.sidebar.title("Sistema de Agendamento")
        opcao = st.sidebar.selectbox("Escolha uma opção", ["Clientes", "Serviços", "Horários", "Profissionais"])

        if opcao == "Clientes":
            ManterClienteUI.main()
        elif opcao == "Serviços":
            ManterServicoUI.main()
        elif opcao == "Horários":
            ManterHorarioUI.main()
        elif opcao == "Profissionais":
            ManterProfissionalUI.main()
            
IndexUI.main()