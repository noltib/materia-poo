class ContaBancaria:
    def __init__(self, titular, numero, saldo=0):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def saque(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor de saque inválido.")

    def exibir_saldo(self):
        print(f"Saldo da conta de {self.titular}: R$ {self.saldo:.2f}")

titular = input("Digite o nome do titular da conta: ")
numero = input("Digite o número da conta: ")
conta = ContaBancaria(titular, numero)

conta.deposito(500)
conta.saque(200)
conta.exibir_saldo()
