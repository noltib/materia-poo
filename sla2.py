import streamlit as st
import json
import os
from datetime import datetime

A_CHAT = "chat.json"

# Função para carregar mensagens
def carregar_mensagens():
    if os.path.exists(A_CHAT):
        with open(A_CHAT, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# Função para salvar mensagens
def salvar_mensagens(mensagens):
    with open(A_CHAT, "w", encoding="utf-8") as f:
        json.dump(mensagens, f, indent=4, ensure_ascii=False)

# Carrega mensagens existentes
mensagens = carregar_mensagens()

# Cabeçalho e login básico
st.title("💬 Sistema de Chat em Streamlit")
usuario = st.text_input("Seu nome:")
destinatario = st.text_input("Com quem quer conversar:")

if usuario and destinatario:
    st.subheader(f"Conversa entre {usuario} e {destinatario}")

    # Filtra apenas as mensagens entre os dois
    conversa = [m for m in mensagens if
                (m["remetente"] == usuario and m["destinatario"] == destinatario) or
                (m["remetente"] == destinatario and m["destinatario"] == usuario)]

    # Exibe as mensagens
    for msg in conversa:
        if msg["remetente"] == usuario:
            with st.chat_message("user"):
                st.markdown(f"**Você:** {msg['mensagem']}")
        else:
            with st.chat_message("assistem", avatar="🗣️"):
                st.markdown(f"**{msg['remetente']}:** {msg['mensagem']}")

    # Campo para enviar nova mensagem
    nova_msg = st.chat_input("Digite sua mensagem...")

    if nova_msg:
        nova = {
            "remetente": usuario,
            "destinatario": destinatario,
            "mensagem": nova_msg,
            "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        mensagens.append(nova)
        salvar_mensagens(mensagens)
        st.rerun()
else:
    st.info("Preencha seu nome e o nome do destinatário para começar o chat.")
