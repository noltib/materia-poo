import streamlit as st
from views import View
import time
import base64

class PerfilClienteUI:
  def main():
    st.header("Meus Dados")
    op = View.cliente_listar_id(st.session_state["cliente_id"])
    st.image(base64.b64decode(op.get_foto()), width=250)
    nome = st.text_input("Informe o novo nome", op.get_nome())
    email = st.text_input("Informe o novo e-mail", op.get_email())
    fone = st.text_input("Informe o novo fone", op.get_fone())
    senha = st.text_input("Informe a nova senha", op.get_senha(), type="password")
    foto = st.file_uploader("adicione sua nova foto", type=["png","jpg","jpeg"], key="atualizar_foto_pc")
    if st.button("Atualizar"):
      foto_base64 = None
      if foto:
          bytes_foto = foto.read()
          foto_base64 = base64.b64encode(bytes_foto).decode("utf-8")
      else:
          foto_base64 = op.get_foto()
      id = op.get_id()
      View.cliente_atualizar(id, nome, email, fone, senha, foto_base64)
      st.success("Cliente atualizado com sucesso")
      time.sleep(2)
      st.rerun()
