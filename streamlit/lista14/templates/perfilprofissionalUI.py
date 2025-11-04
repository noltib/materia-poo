import streamlit as st
from views import View
import base64
import time

class PerfilProfissionalUI:
  def main():
    st.header("Meus Dados")
    op = View.profissional_listar_id(st.session_state["profissional_id"])
    st.image(base64.b64decode(op.get_foto()), width=250)
    nome = st.text_input("Informe o novo nome", op.get_nome())
    email = st.text_input("Informe o novo e-mail", op.get_email())
    especialidade = st.text_input("Informe a nova especialidade", op.get_especialidade())
    conselho = st.text_input("Informe o novo conselho", op.get_conselho())
    senha = st.text_input("Informe a nova senha", op.get_senha(), type="password")
    foto = st.file_uploader("adicione sua nova foto", type=["png","jpg","jpeg"], key="atualizar_foto_pp")
    if st.button("Atualizar"):
      foto_base64 = None
      if foto:
          bytes_foto = foto.read()
          foto_base64 = base64.b64encode(bytes_foto).decode("utf-8")
      else:
          foto_base64 = op.get_foto()
      id = op.get_id()
      View.profissional_atualizar(id, nome, especialidade, conselho, email, senha, foto_base64)
      st.success("Profissional atualizado com sucesso")
      time.sleep(2)
      st.rerun()
