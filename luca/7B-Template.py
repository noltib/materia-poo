# I. Desenvolver em Python um cadastro de contato usando programação em camadas:
from View import View

class ContatoUI:
    @classmethod
    def main(ui):
        x = 0
        ui.View = View
        while x != 10:
            x = ui.menu()
            if x == 1: ui.inserir_ui()
            if x == 2: ui.listar_ui()
            if x == 3: ui.listar_id_ui()
            if x == 4: ui.View.Contato_atualizar()
            if x == 5: ui.View.Contato_excluir()
            if x == 6: ui.View.Contato_pesquisar()
            if x == 7: ui.View.Contato_aniversariantes()
        
    @classmethod
    def menu(ui):
       return int(input("1-Inserir, 2-listar, 3-listar id, 4-atualizar, 5-excluir, 6-pesquisar, 7-aniversariantes, 8-abrir, 9-salvar, 10-sair "))
    
    @classmethod
    def inserir_ui(ui):
        ui.View.Contato_inserir([input("id: "), input("nome: "), input("email: "), input("nascimento: ano, mês, dia: "), input("fone: ")])

    @classmethod
    def listar_ui(ui):
        for c in ui.View.Contato_listar():
            print(c)

    @classmethod
    def listar_id_ui(ui):
        z = input("id: ")
        ui.View.Contato_listar_id(z)

    @classmethod
    def atualizar_ui(ui):
        pass

ContatoUI.main()