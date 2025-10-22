import streamlit as st
from views import View
import time

class PerfilProfissionalUI:
  def main():
    st.header("Meus Dados")
    op = View.profissional_listar_id(st.session_state["usuario_id"])
    nome = st.text_input("Informe o novo nome", op.get_nome())
    email = st.text_input("Informe o novo e-mail", op.get_email())
    especialidade = st.text_input("Informe a nova especialidade", op.get_especialidade())
    conselho = st.text_input("Informe o novo conselho", op.get_conselho())
    senha = st.text_input("Informe a nova senha", op.get_senha(), type="password")
    if st.button("Atualizar"):
      id = op.get_id()
      View.profissional_atualizar(id, nome, especialidade, conselho, email, senha)
      st.success("Profissional atualizado com sucesso")
      time.sleep(2)
      st.rerun()
