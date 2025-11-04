import streamlit as st
from views import View
import time
import base64

class AbrirContaUI:
  def main():
    st.header("Abrir Conta no Sistema")
    nome = st.text_input("Informe o nome")
    email = st.text_input("Informe o e-mail")
    fone = st.text_input("Informe o fone")
    senha = st.text_input("Informe a senha", type="password")
    foto = st.file_uploader("adicione sua foto", type=["png","jpg","jpeg"], key="inserir_foto_ac")
    if st.button("Inserir"):
      foto_base64 = None
      if foto:
        bytes_foto = foto.read()
        foto_base64 = base64.b64encode(bytes_foto).decode("utf-8")
      else:
        foto_base64 = ""
      View.cliente_inserir(nome, email, fone, senha, foto_base64)
      st.success("Conta criada com sucesso")
      time.sleep(2)
      st.rerun()
