class ContaBancaria:
    def __init__(self, nome, numero, saldo=0.0):
        self.__nome = nome
        self.__numero = numero
        self.__saldo = saldo

    def set_nome(self, nome):
        self.__nome = nome

    def set_numero(self, numero):
        self.__numero = numero

    def get_nome(self):
        return self.__nome

    def get_numero(self):
        return self.__numero

    def get_saldo(self):
        return self.__saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
nome = input("digite seu nome: ")
numero = input("digite o numero da conta: ")
conta = ContaBancaria(nome, numero)
a = True
while a == True:
    b = int(input("o que voce quer fazer? 1 = depositar 2 = sacar 3 = mostrar"))
    if b == 1:
        quanto = int(input())
        conta.depositar(quanto)
    if b == 2:
        quanto = int(input())
        conta.sacar(quanto)
    if b == 3:
        print("Titular:", conta.get_nome())
        print("Saldo:", conta.get_saldo())
    if b == 4:
        a = True

