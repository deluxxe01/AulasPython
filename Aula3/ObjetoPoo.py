#Criando uma classe
class Pessoa: 
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def imprimirDados(self):
        print(self.nome, "-", self.idade, "-", self.altura)

objeto_pessoa1 = Pessoa("Ruan", 25, 1.60)
objeto_pessoa2 = Pessoa("Duda", 18, 1.65)
objeto_pessoa3 = Pessoa("Pedro", 5, 1.20)

print(objeto_pessoa1.nome)
objeto_pessoa1.imprimirDados() #Resultado: Ruan - 25 - 1.6
objeto_pessoa2.imprimirDados() #Resultado: Duda - 18 - 1.65
objeto_pessoa3.imprimirDados() #Resultado: Pedro - 5 - 1.2

#Criando uma classe
class vendedor():
    def __init__(self, nome):
        self.nome = nome
        self.vendas = 0

    def vendeu(self, vendas):
        self.vendas = vendas

    def bateu_meta(self, meta):
        if self.vendas > meta:
            print(self.nome,"Bateu a meta")
        else: 
            print(self.nome,"Não bateu a meta")

vendedor1 = vendedor("Lira")
vendedor1.vendeu(1000)
vendedor1.bateu_meta(800)
