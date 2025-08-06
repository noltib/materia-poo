from datetime import datetime, timedelta

class Treino:
    def __init__(self, id: int, dt: datetime, ds: float, t: timedelta):
        self.__id = id
        self.__data = dt
        self.__distancia = ds
        self.__tempo = t

    def get_id(self):
        return self.__id

    def get_data(self):
        return self.__data

    def get_distancia(self):
        return self.__distancia

    def get_tempo(self):
        return self.__tempo

    def set_id(self, id):
        self.__id = id

    def set_data(self, data):
        self.__data = data

    def set_distancia(self, distancia):
        self.__distancia = distancia

    def set_tempo(self, tempo):
        self.__tempo = tempo


    def __str__(self):
        return f"ID: {self.__id}, Data: {self.__data.strftime('%d/%m/%Y')}, Distância: {self.__distancia} km, Tempo: {self.__tempo}"

from datetime import datetime, timedelta

class TreinoUI:
    def __init__(self):
        self.__treinos = []

    def Main(self):
        while True:
            opcao = self.Menu()
            if opcao == 1:
                self.Inserir()
            elif opcao == 2:
                self.Listar()
            elif opcao == 3:
                self.Listar_Id()
            elif opcao == 4:
                self.Atualizar()
            elif opcao == 5:
                self.Excluir()
            elif opcao == 6:
                self.MaisRapido()
            elif opcao == 7:
                print("Saindo...")
                break
            else:
                print("Opção inválida!")

    def Menu(self):
        print("MENU")
        print("1 - Inserir treino")
        print("2 - Listar todos os treinos")
        print("3 - Listar treino por ID")
        print("4 - Atualizar treino")
        print("5 - Excluir treino")
        print("6 - Treino mais rápido")
        print("7 - Sair")
        return int(input("Escolha uma opção: "))

    def Inserir(self):
        id = int(input("ID do treino: "))
        data = datetime.strptime(input("Data (dd/mm/aaaa): "), "%d/%m/%Y")
        distancia = float(input("Distância (km): "))
        tempo_min = float(input("Tempo (min): "))
        tempo = timedelta(minutes=tempo_min)
        treino = Treino(id, data, distancia, tempo)
        self.__treinos.append(treino)
        print("Treino adicionado com sucesso!")

    def Listar(self):
        print("\n--- Lista de Treinos ---")
        for treino in self.__treinos:
            print(treino)

    def Listar_Id(self):
        id = int(input("Digite o ID do treino: "))
        for treino in self.__treinos:
            if treino.get_id() == id:
                print(treino)
                return
        print("Treino não encontrado.")

    def Atualizar(self):
        id = int(input("Digite o ID do treino a ser atualizado: "))
        for treino in self.__treinos:
            if treino.get_id() == id:
                data = datetime.strptime(input("Nova data (dd/mm/aaaa): "), "%d/%m/%Y")
                distancia = float(input("Nova distância (km): "))
                tempo_min = float(input("Novo tempo (min): "))
                tempo = timedelta(minutes=tempo_min)

                treino.set_data(data)
                treino.set_distancia(distancia)
                treino.set_tempo(tempo)
                print("Treino atualizado com sucesso.")
                return
        print("Treino não encontrado.")

    def Excluir(self):
        id = int(input("Digite o ID do treino a ser excluído: "))
        for i, treino in enumerate(self.__treinos):
            if treino.get_id() == id:
                del self.__treinos[i]
                print("Treino excluído.")
                return
        print("Treino não encontrado.")

    def MaisRapido(self):
        if not self.__treinos:
            print("Nenhum treino cadastrado.")
            return

        mais_rapido = self.__treinos[0]
        maior_velocidade = mais_rapido.get_distancia() / (mais_rapido.get_tempo().total_seconds() / 3600)

        for treino in self.__treinos[1:]:
            velocidade = treino.get_distancia() / (treino.get_tempo().total_seconds() / 3600)
            if velocidade > maior_velocidade:
                mais_rapido = treino
                maior_velocidade = velocidade

        print("Treino com maior velocidade média:")
        print(mais_rapido)
        print(f"Velocidade média: {maior_velocidade:.2f} km/h")


app = TreinoUI()
app.Main()
