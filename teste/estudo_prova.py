import datetime
class livro:
    def __init__(self,id,titulo,autor,paginas,data_leitura):
        self.setid(id)
        self.settitulo(titulo)
        self.setautor(autor)
        self.setpaginas(paginas)
        self.setdata(data_leitura)
    def setid(self,id):
        if id >=0:
            self.id = id
        else:
            raise ValueError("id deve ser maior que zero")
    def settitulo(self,titulo):
        if titulo:
            self.titulo = titulo
        else:
            raise ValueError("o titulo nao deve ser vazio")
    def setautor(self,autor):
        if autor:
            self.autor = autor
        else:
            raise ValueError("o autor nao deve ser vazio")
    def setpaginas(self,paginas):
        if paginas >=0:
            self.paginas = paginas
        else:
            raise ValueError("paginas deve ser maior que zero")
    def setdata(self,data):
        self.data = data
    def __str__(self):
        return f"ID: {self.id} \ntitulo: {self.titulo}\nautor: {self.autor}\nnumero de paginas: {self.paginas}\ndata de finalização da leitura: {self.data}"
    

class livroUI:
    livros = []
    def main():
        while True:
            escolha = livroUI.menu()
            if escolha == 1:
                livroUI.inserir()
            if escolha == 2:
                livroUI.listar()
            if escolha == 3:
                livroUI.listar_id()
            if escolha == 4:
                livroUI.atualizar()
            if escolha == 5:
                livroUI.excluir()
            if escolha == 6:
                livroUI.mais_paginas()
            if escolha == 7:
                print("finalizando")
                break
    def menu():
        print("MENU")
        print("1 - Inserir livro")
        print("2 - Listar todos os livros")
        print("3 - Listar livro por ID")
        print("4 - Atualizar livro")
        print("5 - Excluir livro")
        print("6 - Livro com mais páginas")
        print("7 - Sair")
        op = int(input())
        return op
    def inserir():
        id = int(input("Digite o id: "))
        titulo = input("Digite o titulo: ")
        autor = input("Digite o autor: ")
        paginas = int(input("Digite o numero de paginas: "))
        data = datetime.datetime.strptime(input("Digite a data da finalização da leitura (DD/MM/AAAA): "), "%d/%m/%Y")
        p = livro(id,titulo,autor,paginas,data)
        livroUI.livros.append(p)
        print("livro registrado com sucesso!")
    def listar():
        if livroUI.livros:
            for i in livroUI.livros:
                print(i)
        else:
            print("sem livros registrados")
    def listar_id():
        id = int(input())
        if livroUI.livros:
            for i in livroUI.livros:
                if i.id == id:
                    print(i)
        else:
            print("sem livros registrados")
    def atualizar():
        pass
    def excluir():
        pass
    def mais_paginas():
        pass
v = livroUI
v.main()