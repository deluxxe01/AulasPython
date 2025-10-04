# Criar uma classe que representa uma garrafa de água e permite enchê-la ou beber dela.
# Criar uma classe Garrafa.
# A garrafa tem:
# um atributo volume (inicialmente começa vazia, ou seja, 0).
# Métodos:
# encher(): coloca água na garrafa até 100.
# beber(qtd): diminui a quantidade de água se houver suficiente.
# mostrar_volume(): mostra quanto de água há na garrafa.

#Criando a classe
class Garrafa: #1
    #Atributo volume usando o construtor
    def __init__(self): #4
        self.volume = 0  # Começa com o valor vazio

    #Ação encher adcionando o valor no volume
    def encher(self): #6
        self.volume = 100  # Enche a garrafa
        print("Garrafa cheia.")

    #Ação beber diminuindo o valor no volume
    def beber(self, qnt): #9
        #Validação da quantidade de volume que tem
        if qnt <= self.volume:
            self.volume -= qnt
            print(f"Você bebeu {qnt}ml de água.")
        else:
            print("Não há água suficiente para beber essa quantidade.")

    def mostrar_volume(self): #11
        print(f"A garrafa agora contém {self.volume}ml de água.")

g = Garrafa() #2 
g.mostrar_volume() #3 Resultado: 0 pois o volume inical é esse
g.encher() #5 Resultado: 100 pois é executado a ação encher 
x = int(input("Digite quantos ml quer beber: ")) #7
g.beber(x) #8 #Valor colocado para encher
g.mostrar_volume() #10