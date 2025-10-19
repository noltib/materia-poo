import streamlit as st
import pandas as pd
from views import View
import time
from datetime import datetime, date

class GerenciarAgendaUI:
    def main():
        st.header("Cadastro de Horários")
        tab1, tab2= st.tabs(["Listar", "Inserir"])
        with tab1: GerenciarAgendaUI.listar()
        with tab2: GerenciarAgendaUI.inserir()

    def listar():
        profissional = View.profissional_listar_id(st.session_state["usuario_id"])
        if profissional is None:
            st.warning("Nenhum profissional logado.")
            return

        horarios = View.horario_listar()
        if len(horarios) == 0:
            st.info("Nenhum horário cadastrado.")
            return

        horarios_profissional = [h for h in horarios if h.get_id_profissional() == profissional.get_id()]
        if len(horarios_profissional) == 0:
            st.info("Você ainda não abriu horários na sua agenda.")
            return

        dic = []
        for obj in horarios_profissional:
            cliente = View.cliente_listar_id(obj.get_id_cliente())
            servico = View.servico_listar_id(obj.get_id_servico())

            dic.append({
                "id": obj.get_id(),
                "data": obj.get_data(),
                "confirmado": obj.get_confirmado(),
                "cliente": cliente.get_nome() if cliente else None,
                "serviço": servico.get_descricao() if servico else None
            })

        df = pd.DataFrame(dic)
        st.dataframe(df, hide_index=True)

    def inserir():
        st.subheader("Abrir Minha Agenda")

        profissional = View.profissional_listar_id(st.session_state["usuario_id"])
        if profissional is None:
            st.warning("Nenhum profissional logado.")
            return

        data = st.date_input("Informe o dia do atendimento", date.today())
        hora_inicial = st.time_input("Hora inicial do atendimento")
        hora_final = st.time_input("Hora final do atendimento")
        intervalo = st.number_input("Intervalo entre atendimentos (em minutos)", min_value=5, step=5)

        if st.button("Gerar horários"):
            from datetime import datetime, timedelta

            inicio = datetime.combine(data, hora_inicial)
            fim = datetime.combine(data, hora_final)
            horarios_gerados = []

            while inicio < fim:
                View.horario_inserir(inicio, False, None, None, profissional.get_id())
                horarios_gerados.append(inicio.strftime("%H:%M"))
                inicio += timedelta(minutes=intervalo)

            st.success(f"Foram inseridos {len(horarios_gerados)} horários na agenda!")
