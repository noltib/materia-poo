import json
from datetime import datetime

class Chat:
    def __init__(self, remetente, destinatario, texto, timestamp=None):
        self.remetente = remetente
        self.destinatario = destinatario
        self.texto = texto
        self.timestamp = timestamp or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def get_remetente(self):
        return self.remetente
    
    def get_destinatario(self):
        return self.destinatario

    def get_mensagem(self):
        return self.texto

    def get_data(self):
        return self.timestamp
    
    def to_json(self):
        return {
            "remetente": self.remetente,
            "destinatario": self.destinatario,
            "mensagem": self.texto,
            "data": self.timestamp
        }

    @staticmethod
    def from_json(d):
        return Chat(d["remetente"], d["destinatario"], d["mensagem"], d["data"])


class ChatDAO:

    @staticmethod
    def carregar_todas():
        try:
            with open("chat.json", "r", encoding="utf-8") as f:
                dados = json.load(f)
                return [Chat.from_json(m) for m in dados]
        except FileNotFoundError:
            return []

    @staticmethod
    def salvar(mensagem: Chat):
        mensagens = ChatDAO.carregar_todas()
        mensagens.append(mensagem)
        with open("chat.json", "w", encoding="utf-8") as f:
            json.dump([m.to_json() for m in mensagens], f, indent=4, ensure_ascii=False)

    @staticmethod
    def filtrar_conversa(usuario, destinatario):
        todas = ChatDAO.carregar_todas()
        return [
            m for m in todas
            if (m.remetente == usuario and m.destinatario == destinatario)
            or (m.remetente == destinatario and m.destinatario == usuario)
        ]