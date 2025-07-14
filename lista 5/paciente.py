import datetime

class Paciente:
    def __init__(self, nome, cpf, telefone, nasc):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.nasc = nasc

    def alterar(self, n_nome, n_cpf, n_telefone, n_nasc):
        self.nome = n_nome
        self.cpf = n_cpf
        self.telefone = n_telefone
        self.nasc = n_nasc        

    def idade(self):
        hoje = datetime.date.today()
        nascimento = self.nasc.date()
        idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
        return idade

    def ToString(self):
        return f"Olá {self.nome}!\nVocê tem {self.idade()} anos.\nCPF: {self.cpf}\nTelefone: {self.telefone}"

class PacienteUI:
    pacientes = []

    @staticmethod
    def main():
        while True:
            op = PacienteUI.menu()
            if op == 1:
                PacienteUI.registrar()
            elif op == 2:
                PacienteUI.alterar()
            elif op == 3:
                PacienteUI.mostrar()
            elif op == 4:
                print("Programa finalizado.")
                break
            else:
                print("Opção inválida!")

    @staticmethod
    def menu():
        print("MENU:")
        print("1 - Registrar novo paciente")
        print("2 - Alterar paciente existente")
        print("3 - Mostrar paciente")
        print("4 - Sair")
        return int(input("Digite sua opção: "))

    @staticmethod
    def registrar():
        nome = input("Digite o nome: ")
        cpf = input("Digite o CPF: ")
        telefone = input("Digite o telefone: ")
        d_nasc = datetime.datetime.strptime(input("Digite a data de nascimento (DD/MM/AAAA): "), "%d/%m/%Y")
        p = Paciente(nome, cpf, telefone, d_nasc)
        PacienteUI.pacientes.append(p)
        print("Paciente registrado com sucesso!")

    @staticmethod
    def alterar():
        cpf = input("Digite o CPF do paciente que deseja alterar: ")
        for p in PacienteUI.pacientes:
            if p.cpf == cpf:
                print("Paciente encontrado. Digite os novos dados:")
                n_nome = input("Novo nome: ")
                n_cpf = input("Novo CPF: ")
                n_telefone = input("Novo telefone: ")
                n_d_nasc = datetime.datetime.strptime(input("Nova data de nascimento (DD/MM/AAAA): "), "%d/%m/%Y")
                p.alterar(n_nome, n_cpf, n_telefone, n_d_nasc)
                print("Dados alterados com sucesso!")
                return
        print("Paciente com esse CPF não encontrado.")

    @staticmethod
    def mostrar():
        cpf = input("Digite o CPF do paciente que deseja visualizar: ")
        for p in PacienteUI.pacientes:
            if p.cpf == cpf:
                print(p.ToString())
                return
        print("Paciente com esse CPF não encontrado.")

PacienteUI.main()
