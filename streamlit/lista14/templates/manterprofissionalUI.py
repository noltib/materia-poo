import streamlit as st
import pandas as pd
from views import View
import time
import base64

class ManterProfissionalUI:
    def main():
        st.header("Cadastro de profissionais")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterProfissionalUI.listar()
        with tab2: ManterProfissionalUI.inserir()
        with tab3: ManterProfissionalUI.atualizar()
        with tab4: ManterProfissionalUI.excluir()

    def listar():
        profissionais = View.profissional_listar()
        if len(profissionais) == 0: st.write("Nenhum profissional cadastrado")
        else:
            list_dic = []
            for obj in profissionais: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df.drop(columns=["foto"], errors="ignore"), hide_index=True)

    def inserir():
        nome = st.text_input("Informe o nome")
        especialidade = st.text_input("Informe a especialidade")
        conselho = st.text_input("Informe o conselho")
        email = st.text_input("Informe o email")
        senha = st.text_input("Informe a senha", type="password")
        foto = st.file_uploader("adicione sua foto", type=["png","jpg","jpeg"], key="inserir_foto_mp")
        if st.button("Inserir"):
            try:
                foto_base64 = None
                if foto:
                    bytes_foto = foto.read()
                    foto_base64 = base64.b64encode(bytes_foto).decode("utf-8")
                else:
                    foto_base64 = ""
                View.profissional_inserir(nome, especialidade, conselho, email, senha, foto_base64)
                st.success("Profissional inserido com sucesso")
            except ValueError as erro:
                st.error(erro)
            time.sleep(2)
            st.rerun()

    def atualizar():
        profissionais = View.profissional_listar()
        if len(profissionais) == 0: st.write("Nenhum profissional cadastrado")
        else:
            op = st.selectbox("Atualização de profissionais", profissionais)
            nome = st.text_input("Informe o novo nome", op.get_nome())
            especialidade = st.text_input("Informe a nova especialidade", op.get_especialidade())
            conselho = st.text_input("Informe o novo conselho", op.get_conselho())
            email = st.text_input("Informe o novo email", op.get_email())
            senha = st.text_input("Informe a nova senha", op.get_senha(), type="password")
            foto = st.file_uploader("adicione sua nova foto", type=["png","jpg","jpeg"], key="atualizar_foto_mp")

            if st.button("Atualizar"):
                try:
                    foto_base64 = None
                    if foto:
                        bytes_foto = foto.read()
                        foto_base64 = base64.b64encode(bytes_foto).decode("utf-8")
                    else:
                        foto_base64 = op.get_foto()
                    id = op.get_id()
                    View.profissional_atualizar(id, nome, especialidade, conselho, email, senha, foto_base64)
                    st.success("Profissional atualizado com sucesso")
                except ValueError as erro:
                    st.error(erro)
                time.sleep(2)
                st.rerun()

    def excluir():
        profissionais = View.profissional_listar()
        if len(profissionais) == 0: st.write("Nenhum profissional cadastrado")
        else:
            op = st.selectbox("Exclusão de profissionais", profissionais)
            if st.button("Excluir"):
                try:
                    id = op.get_id()
                    View.profissional_excluir(id)
                    st.success("Profissional excluído com sucesso")
                except ValueError as erro:
                    st.error(erro)
                time.sleep(2)
                st.rerun()
