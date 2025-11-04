import streamlit as st
from views import View
import time

class AgendarServicoUI:
    def main():
        st.header("Agendar Serviço")
        profs = View.profissional_listar()
        if len(profs) == 0: st.write("Nenhum profissional cadastrado")
        else:
            profissional = st.selectbox("Informe o profissional", profs)
            horarios = View.horario_agendar_horario(profissional.get_id())
            if len(horarios) == 0: st.write("Nenhum horário disponível")
            else:
                horario = st.selectbox("Informe o horário", horarios)
                servicos = View.servico_listar()
                servico = st.selectbox("Informe o serviço", servicos)
                if st.button("Agendar"):
                    View.horario_atualizar(horario.get_id(),
                        horario.get_data(), False,
                        st.session_state["profissional_id"], 
                        servico.get_id(), profissional.get_id())
                    st.success("Horário agendado com sucesso")
                    time.sleep(2)
                    st.rerun()                