class View:
    @staticmethod
    def menu():
        print("\n--- MENU ---")
        print("1. Inserir")
        print("2. Listar todos")
        print("3. Listar por ID")
        print("4. Atualizar")
        print("5. Excluir")
        print("6. Pesquisar por nome")
        print("7. Aniversariantes do mês")
        print("8. Abrir arquivo")
        print("9. Salvar arquivo")
        print("0. Sair")
        op = int(input("Opção: "))
        return op
