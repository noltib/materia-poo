# view.py

class View:
    @staticmethod
    def mostrar_contato(contato):
        print(contato)

    @staticmethod
    def mostrar_lista(contatos):
        for c in contatos:
            print(c)
