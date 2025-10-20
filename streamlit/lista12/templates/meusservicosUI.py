import streamlit as st
import pandas as pd
from views import View

class MeusServicosUI:
    def main():
        st.header("Meus Serviços")

        cliente = View.cliente_listar_id(st.session_state["usuario_id"])
        if cliente is None:
            st.warning("Nenhum cliente logado.")
            return

        horarios = View.horario_listar()
        if len(horarios) == 0:
            st.info("Nenhum horário cadastrado.")
            return

        horarios_cliente = [h for h in horarios if h.get_id_cliente() == cliente.get_id()]
        if len(horarios_cliente) == 0:
            st.info("Você ainda não possui serviços agendados.")
            return

        dic = []
        for obj in horarios_cliente:
            servico = View.servico_listar_id(obj.get_id_servico())
            profissional = View.profissional_listar_id(obj.get_id_profissional())

            dic.append({
                "id": obj.get_id(),
                "data": obj.get_data(),
                "confirmado": obj.get_confirmado(),
                "serviço": servico.get_descricao() if servico else None,
                "profissional": profissional.get_nome() if profissional else None
            })

        df = pd.DataFrame(dic)
        st.dataframe(df, hide_index=True)
