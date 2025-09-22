from models import Cliente, ClienteDAO

def cliente_inserir(nome):
    ClienteDAO.inserir(Cliente(0, nome))

def cliente_listar():
    return ClienteDAO.listar()
