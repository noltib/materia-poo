import streamlit as st
import sqlite3
from datetime import datetime

# ---- BANCO DE DADOS ----
def init_db():
    conn = sqlite3.connect("chat.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS mensagens (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    remetente TEXT,
                    destinatario TEXT,
                    mensagem TEXT,
                    timestamp TEXT
                )''')
    conn.commit()
    conn.close()

def salvar_mensagem(remetente, destinatario, mensagem):
    conn = sqlite3.connect("chat.db")
    c = conn.cursor()
    c.execute("INSERT INTO mensagens (remetente, destinatario, mensagem, timestamp) VALUES (?, ?, ?, ?)",
              (remetente, destinatario, mensagem, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

def carregar_mensagens(remetente, destinatario):
    conn = sqlite3.connect("chat.db")
    c = conn.cursor()
    c.execute('''SELECT remetente, mensagem, timestamp FROM mensagens 
                 WHERE (remetente = ? AND destinatario = ?) OR (remetente = ? AND destinatario = ?)
                 ORDER BY id ASC''', (remetente, destinatario, destinatario, remetente))
    mensagens = c.fetchall()
    conn.close()
    return mensagens

# ---- INTERFACE STREAMLIT ----
st.title("💬 Chat interno de agendamentos")

init_db()

# Simulação de login simples
usuario = st.text_input("Seu nome:")
destinatario = st.text_input("Com quem quer conversar:")

if usuario and destinatario:
    st.subheader(f"Conversando com {destinatario}")

    mensagens = carregar_mensagens(usuario, destinatario)
    for remetente, msg, time in mensagens:
        if remetente == usuario:
            st.markdown(f"<div style='text-align:right; color:blue;'>Você ({time}): {msg}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div style='text-align:left; color:green;'>{remetente} ({time}): {msg}</div>", unsafe_allow_html=True)

    nova_msg = st.text_input("Digite sua mensagem:")
    if st.button("Enviar"):
        if nova_msg.strip():
            salvar_mensagem(usuario, destinatario, nova_msg)
            st.rerun()