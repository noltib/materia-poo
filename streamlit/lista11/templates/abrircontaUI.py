import streamlit as st
from views import View
import time

class AbrirContaUI:
  def main():
    st.header("Abrir Conta no Sistema")
    nome = st.text_input("Informe o nome")
    email = st.text_input("Informe o e-mail")
    fone = st.text_input("Informe o fone")
    senha = st.text_input("Informe a senha", type="password")
    if st.button("Inserir"):
      View.cliente_inserir(nome, email, fone, senha)
      st.success("Conta criada com sucesso")
      time.sleep(2)
      st.rerun()
