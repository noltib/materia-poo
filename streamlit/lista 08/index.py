import streamlit as st
import datetime 
from streamlit_extras.let_it_rain import rain

class Paciente:
    def __init__(self, nome, cpf, fone, nascimento):
        self.__nome = nome
        self.__cpf = cpf
        self.__fone = fone
        self.__nasc = nascimento

    @property
    def nascimento(self):
        return self.__nasc

    def idade(self):
        hoje = datetime.date.today()
        nascimento = self.__nasc
        idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
        
        if hoje.month == nascimento.month and hoje.day == nascimento.day:
            return f"🎉 Parabéns, {self.__nome}! Você está completando {idade} anos hoje! 🥳"
        else:
            return f"Idade: {idade} anos"
    
    def __str__(self):
        return self.idade()

nome = st.text_input("Nome:")
cpf = st.text_input("CPF:")
fone = st.text_input("Fone:")
nascimento = st.date_input("Nascimento:", min_value=datetime.date(1925, 1, 1))

if st.button("Enviar"):
    p = Paciente(nome, cpf, fone, nascimento)
    st.write(p)
    
    hoje = datetime.date.today()
    if hoje.month == p.nascimento.month and hoje.day == p.nascimento.day:
        rain(
            emoji="🥳",
            font_size=54,
            falling_speed=3,
            animation_length="infinite",
        )
