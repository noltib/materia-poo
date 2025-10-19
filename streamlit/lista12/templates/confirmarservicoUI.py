import streamlit as st
from views import View

class ConfirmarServicoUI:
    def main():
        st.header("Confirmar Serviço")

        # Recupera o profissional logado
        profissional = View.profissional_listar_id(st.session_state["usuario_id"])
        if profissional is None:
            st.warning("Nenhum profissional logado.")
            return

        # Lista todos os horários do sistema
        horarios = View.horario_listar()
        if len(horarios) == 0:
            st.info("Nenhum horário cadastrado.")
            return

        # Filtra apenas os horários do profissional que já tenham cliente
        horarios_profissional = [
            h for h in horarios
            if h.get_id_profissional() == profissional.get_id() and h.get_id_cliente() is not None
        ]
        if len(horarios_profissional) == 0:
            st.info("Você não possui horários agendados com clientes.")
            return

        # Selectbox para escolher o horário
        op = st.selectbox(
            "Informe o horário",
            horarios_profissional,
            format_func=lambda h: f"{h.get_id()} - {h.get_data().strftime('%d/%m/%Y %H:%M')} - {h.get_confirmado()}"
        )

        # Carrega o cliente desse horário
        cliente = View.cliente_listar_id(op.get_id_cliente())
        clientes_op = []
        if cliente is not None:
            clientes_op.append(cliente)

        cliente_selecionado = st.selectbox(
            "Cliente",
            clientes_op,
            format_func=lambda c: f"{c.get_id()} - {c.get_nome()} - {c.get_email()} - {c.get_fone()}"
        )

        # Botão para confirmar
        if st.button("Confirmar"):
            View.horario_atualizar(
                op.get_id(),
                op.get_data(),
                True,  # confirmando o serviço
                op.get_id_cliente(),
                op.get_id_servico(),
                op.get_id_profissional()
            )
            st.success("Serviço confirmado com sucesso!")