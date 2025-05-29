class agua():
	def __int__(self):
		self.mes = 0
		self.ano = 0
		self.consumo = 0
	def calculo(self):
		if self.consumo <=10:
			print(f"o valor da conta de energia da data {self.mes}/{self.ano} foi R$38")
		elif 10 < self.consumo <=20:
			print(f"o valor da conta de energia da data {self.mes}/{self.ano} foi R${(self.consumo-10)*5+38}")
		elif self.consumo >= 20:
			print(f"o valor da conta de energia da data {self.mes}/{self.ano} foi R${(self.consumo-20)*5+38+45}")

x = agua()
x.mes = int(input("Digite o mês da conta: "))
x.ano = int(input("Digite o ano da conta: "))
x.consumo = int(input("Digite o seu  consumo: "))
x.calculo()

