import datetime
from enum import Enum
from decimal import Decimal

class Pagamento(Enum):
    EmAberto = 0
    PagoParcial = 1
    Pago = 2

class Boleto:
    def __init__(self, cod: str, emissao: datetime.datetime, venc: datetime.datetime, valor: Decimal):
        self.codBarras = cod
        self.dataEmissao = emissao
        self.dataVencimento = venc
        self.valorBoleto = valor
        self.valorPago = Decimal('0.00')
        self.dataPago = None
        self.situacaoPagamento = Pagamento.EmAberto

    def pagar(self, valor: Decimal):
        self.valorPago += valor
        self.dataPago = datetime.datetime.now()
        if self.valorPago == 0:
            self.situacaoPagamento = Pagamento.EmAberto
        elif self.valorPago < self.valorBoleto:
            self.situacaoPagamento = Pagamento.PagoParcial
        else:
            self.situacaoPagamento = Pagamento.Pago

    def situacao(self):
        return self.situacaoPagamento

    def __str__(self):
        pago = f"{self.valorPago:.2f}"
        valor = f"{self.valorBoleto:.2f}"
        data_pagamento = self.dataPago.strftime("%d/%m/%Y %H:%M") if self.dataPago else "Não pago"
        return (
            f"\nBoleto: {self.codBarras}\n"
            f"Emissão: {self.dataEmissao.strftime('%d/%m/%Y')}\n"
            f"Vencimento: {self.dataVencimento.strftime('%d/%m/%Y')}\n"
            f"Valor: R$ {valor}\n"
            f"Valor pago: R$ {pago}\n"
            f"Data de pagamento: {data_pagamento}\n"
            f"Situação: {self.situacaoPagamento.name}\n"
        )

class BoletoUI:
    boletos = []

    @staticmethod
    def main():
        while True:
            op = BoletoUI.menu()
            if op == 1:
                BoletoUI.registrar()
            elif op == 2:
                BoletoUI.pagar()
            elif op == 3:
                BoletoUI.mostrar()
            elif op == 4:
                print("Programa finalizado.")
                break
            else:
                print("Opção inválida!")

    @staticmethod
    def menu():
        print("\n=== MENU ===")
        print("1 - Registrar novo boleto")
        print("2 - Pagar boleto")
        print("3 - Mostrar boleto")
        print("4 - Sair")
        return int(input("Digite sua opção: "))

    @staticmethod
    def registrar():
        cod = input("Digite o código de barras: ")
        emissao = datetime.datetime.strptime(input("Data de emissão (DD/MM/AAAA): "), "%d/%m/%Y")
        venc = datetime.datetime.strptime(input("Data de vencimento (DD/MM/AAAA): "), "%d/%m/%Y")
        valor = Decimal(input("Valor do boleto: ").replace(",", "."))
        b = Boleto(cod, emissao, venc, valor)
        BoletoUI.boletos.append(b)
        print("Boleto registrado com sucesso!")

    @staticmethod
    def pagar():
        cod = input("Digite o código de barras do boleto: ")
        for b in BoletoUI.boletos:
            if b.codBarras == cod:
                valor = Decimal(input("Digite o valor a pagar: ").replace(",", "."))
                b.pagar(valor)
                print("Pagamento realizado com sucesso!")
                return
        print("Boleto não encontrado.")

    @staticmethod
    def mostrar():
        cod = input("Digite o código de barras do boleto: ")
        for b in BoletoUI.boletos:
            if b.codBarras == cod:
                print(b)
                return
        print("Boleto não encontrado.")

BoletoUI.main()
