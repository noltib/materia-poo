import streamlit as st
import pandas as pd
from views import View
import time
from datetime import datetime

class ManterHorarioUI:
    def main():
        st.header("Cadastro de Horários")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterHorarioUI.listar()
        with tab2: ManterHorarioUI.inserir()
        with tab3: ManterHorarioUI.atualizar()
        with tab4: ManterHorarioUI.excluir()

    def listar():
        horarios = View.horario_listar()
        if len(horarios) == 0: 
            st.write("Nenhum horário cadastrado")
        else: 
            dic = []
            for obj in horarios:
                cliente = View.cliente_listar_id(obj.get_id_cliente())
                servico = View.servico_listar_id(obj.get_id_servico())
                profissional = View.profissional_listar_id(obj.get_id_profissional())
                if cliente != None: cliente = cliente.get_nome()
                if profissional != None: profissional = profissional.get_nome()
                if servico != None: servico = servico.get_descricao()
                dic.append({
                    "id" : obj.get_id(), 
                    "data" : obj.get_data(), 
                    "confirmado" : obj.get_confirmado(), 
                    "cliente" : cliente, 
                    "serviço" : servico,
                    "profissional" : profissional
                })
            df = pd.DataFrame(dic)
            st.dataframe(df, hide_index=True)

    def inserir():
        clientes = View.cliente_listar()
        servicos = View.servico_listar()
        profissional = View.profissional_listar()
        data = st.text_input("Informe a data e horário do serviço", datetime.now().strftime("%d/%m/%Y %H:%M"))
        confirmado = st.checkbox("Confirmado")
        cliente = st.selectbox("Informe o cliente", clientes, index = None)
        profissional = st.selectbox("Informe o profissional", profissional, index = None)
        servico = st.selectbox("Informe o serviço", servicos, index = None)

        if st.button("Inserir"):
            id_cliente = None
            id_servico = None
            if cliente != None: id_cliente = cliente.get_id()
            if profissional != None: id_profissional = profissional.get_id()
            if servico != None: id_servico = servico.get_id()
            View.horario_inserir(datetime.strptime(data, "%d/%m/%Y %H:%M"), confirmado, id_cliente, id_servico, id_profissional)
            st.success("Horário inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        horarios = View.horario_listar()
        if len(horarios) == 0: 
            st.write("Nenhum horário cadastrado")
        else:
            clientes = View.cliente_listar()
            profissionais = View.profissional_listar()
            servicos = View.servico_listar()
            op = st.selectbox("Atualização de Horários", horarios)

            data = st.text_input("Informe a nova data e horário do serviço", op.get_data().strftime("%d/%m/%Y %H:%M"))
            confirmado = st.checkbox("Nova confirmação", op.get_confirmado())

            id_cliente = None if op.get_id_cliente() in [0, None] else op.get_id_cliente()
            id_profissional = None if op.get_id_profissional() in [0, None] else op.get_id_profissional()
            id_servico = None if op.get_id_servico() in [0, None] else op.get_id_servico()

            cliente = st.selectbox("Informe o novo cliente", clientes, next((i for i, c in enumerate(clientes) if c.get_id() == id_cliente), None))
            profissional = st.selectbox("Informe o novo profissional", profissionais, next((i for i, p in enumerate(profissionais) if p.get_id() == id_profissional), None))
            servico = st.selectbox("Informe o novo serviço", servicos, next((i for i, s in enumerate(servicos) if s.get_id() == id_servico), None))

            if st.button("Atualizar"):
                id_cliente = None
                id_profissional = None
                id_servico = None
                if cliente != None: id_cliente = cliente.get_id()
                if profissional != None: id_profissional = profissional.get_id()
                if servico != None: id_servico = servico.get_id()
                View.horario_atualizar(op.get_id(), datetime.strptime(data, "%d/%m/%Y %H:%M"), confirmado, id_cliente, id_servico)
                st.success("Horário atualizado com sucesso")

    def excluir():
        horarios = View.horario_listar()
        if len(horarios) == 0: 
            st.write("Nenhum horário cadastrado")
        else:
            op = st.selectbox("Exclusão de Horários", horarios)
            if st.button("Excluir"):
                View.horario_excluir(op.get_id())
                st.success("Horário excluído com sucesso")
                time.sleep(2)
                st.rerun()
