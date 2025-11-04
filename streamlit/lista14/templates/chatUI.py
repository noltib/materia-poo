import streamlit as st
import time
from views import View
from PIL import Image
from io import BytesIO
import base64

class ChatUI:
    def main():
        st.header("Chat entre Cliente e Profissional")
        profs = View.profissional_listar()
        if len(profs) == 0: st.write("Nenhum profissional cadastrado")
        usuario_c = View.cliente_listar_id(st.session_state["cliente_id"])
        usuario, n_usuario, f_usuario = usuario_c.get_email(), usuario_c.get_nome(), usuario_c.get_foto()
        img_bytes_u = base64.b64decode(f_usuario)
        usuario_i = Image.open(BytesIO(img_bytes_u))
        destinatario = st.selectbox("Informe o profissional", profs)
        destinatario, n_destinatario, f_destinatario= destinatario.get_email() if destinatario else None, destinatario.get_nome() if destinatario else None, destinatario.get_foto() if destinatario else None
        img_bytes_d = base64.b64decode(f_destinatario)
        destinatario_i = Image.open(BytesIO(img_bytes_d))
        if usuario and destinatario:

            st.subheader(f"Conversa entre {n_usuario} e {n_destinatario}")

            conversa = View.chat_filtrar_conversa(usuario, destinatario)

            for msg in conversa:
                if msg.get_remetente() == usuario:
                    with st.chat_message("user", avatar=usuario_i):
                        st.markdown(f"**Você:** {msg.get_mensagem()}")
                else:
                    with st.chat_message("assistant", avatar=destinatario_i):
                        st.markdown(f"**{n_destinatario}:** {msg.get_mensagem()}")
            
            nova_msg = st.chat_input("Digite sua mensagem...")

            if nova_msg:
                View.chat_salvar_mensagem(usuario, destinatario, nova_msg)
                st.rerun()
            tempo = 4
            ultimo = time.time()
            while True:
                agora = time.time()
                if agora - ultimo > tempo:
                    st.rerun()
        else:
            st.info("Preencha seu nome e o nome do destinatário para começar o chat.")