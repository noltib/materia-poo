import streamlit as st
from views import View

class LoginUI:

    @staticmethod
    def main():
      st.header("Entrar no Sistema")
      email = st.text_input("E-mail", key="login_email")
      senha = st.text_input("Senha", type="password", key="login_senha")

      if st.button("Entrar"):
          c = View.cliente_autenticar(email, senha)
          if c is None:
              st.error("E-mail ou senha inválidos")
          else:
              st.session_state["cliente_id"] = c["id"]
              st.session_state["cliente_nome"] = c["nome"]
              st.rerun()
