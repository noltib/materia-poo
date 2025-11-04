import streamlit as st
import pandas as pd
from views import View
import time
import base64

class ManterClienteUI:
    def main():
        st.header("Cadastro de Clientes")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterClienteUI.listar()
        with tab2: ManterClienteUI.inserir()
        with tab3: ManterClienteUI.atualizar()
        with tab4: ManterClienteUI.excluir()

    def listar():
        clientes = View.cliente_listar()
        if len(clientes) == 0: st.write("Nenhum cliente cadastrado")
        else:
            list_dic = []
            for obj in clientes: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df.drop(columns=["foto"], errors="ignore"), hide_index=True)

    def inserir():
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o fone")
        senha = st.text_input("Informe a senha", type="password")
        foto = st.file_uploader("adicione sua foto", type=["png","jpg","jpeg"], key="inserir_foto_mc")
        
        if st.button("Inserir"):
            try:
                foto_base64 = None
                if foto:
                    bytes_foto = foto.read()
                    foto_base64 = base64.b64encode(bytes_foto).decode("utf-8")
                else:
                    foto_base64 = ""
                View.cliente_inserir(nome, email, fone, senha, foto_base64)
                st.success("Cliente inserido com sucesso!")
            except ValueError as erro:
                st.error(erro)
            time.sleep(2)
            st.rerun()

    def atualizar():
        clientes = View.cliente_listar()
        if len(clientes) == 0: st.write("Nenhum cliente cadastrado")
        else:
            op = st.selectbox("Atualização de Clientes", clientes)
            nome = st.text_input("Novo nome", op.get_nome())
            email = st.text_input("Novo e-mail", op.get_email())
            fone = st.text_input("Novo fone", op.get_fone())
            senha = st.text_input("Nova senha", op.get_senha(), type="password")
            foto = st.file_uploader("adicione sua foto", type=["png","jpg","jpeg"], key="atualizar_foto_mc")
            if st.button("Atualizar"):
                try:
                    foto_base64 = None
                    if foto:
                        bytes_foto = foto.read()
                        foto_base64 = base64.b64encode(bytes_foto).decode("utf-8")
                    else:
                        foto_base64 = op.get_foto()
                    id = op.get_id()
                    View.cliente_atualizar(id, nome, email, fone, senha, foto_base64)
                    st.success("Cliente atualizado com sucesso")
                except ValueError as erro:
                    st.error(erro)
                time.sleep(2)
                st.rerun()


    def excluir():
        clientes = View.cliente_listar()
        if len(clientes) == 0: st.write("Nenhum cliente cadastrado")
        else:
            op = st.selectbox("Exclusão de Clientes", clientes)
            if st.button("Excluir"):
                try:
                    id = op.get_id()
                    View.cliente_excluir(id)
                    st.success("Cliente excluído com sucesso")
                except ValueError as erro:
                    st.error(erro)
                time.sleep(2)
                st.rerun()
