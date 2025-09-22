class Cliente:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
    def __str__(self):
        return f"{self.id} - {self.nome}"

class ClienteDAO:
    __objetos = []
    @classmethod
    def inserir(cls, obj):
        id = max((aux.id for aux in cls.__objetos), default=0)
        obj.id = id + 1
        cls.__objetos.append(obj)
    @classmethod
    def listar(cls):
        return cls.__objetos
