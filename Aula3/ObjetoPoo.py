#ORIENTAÇÃO A OBJETO
#Criando uma classe
class Pessoa: 
    #Criando atributo 
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def imprimirDados(self):
        print(self.nome, "-", self.idade, "-", self.altura)

#Adcionando valores aos atributos
objeto_pessoa1 = Pessoa("Ruan", 25, 1.60)
objeto_pessoa2 = Pessoa("Duda", 18, 1.65)
objeto_pessoa3 = Pessoa("Pedro", 5, 1.20)

print(objeto_pessoa1.nome)
objeto_pessoa1.imprimirDados() #Resultado: Ruan - 25 - 1.6
objeto_pessoa2.imprimirDados() #Resultado: Duda - 18 - 1.65
objeto_pessoa3.imprimirDados() #Resultado: Pedro - 5 - 1.2

#Criando uma classe
class vendedor(): #1
     #Atributo
     def __init__(self, nome): #3
         self.nome = nome
         self.vendas = 0
     #Ação
     def vendeu(self, vendas): #5
         self.vendas = vendas
     #Ação
     def bateu_meta(self, meta): #7
         if self.vendas > meta:  #8
             print(self.nome,"Bateu a meta")
         else: #9
             print(self.nome,"Não bateu a meta")

vendedor1 = vendedor(input("Digite o nome do vendedor: ")) #2
vendedor1.vendeu(float(input("Digite o valor das vendas: "))) #4
vendedor1.bateu_meta(float(input("Digite a meta a ser batida: "))) #6


#Criando uma classe chamada circulo
class Circulo():
    #O valor de pi é constante
    pi = 3.14
    #Quando um objeto desta classe for criado, este metodo será executado e o valor default do raio sera 5
    def __init__(self,raio = 5):
        self.raio = raio
    #Esse método calcula a área 
    def area(self):
        return(self.raio * self.raio) * Circulo.pi
    #Método para gerar um novo (colocar o setraio digitado no atributo raio)
    def setRaio(self, raio):
        self.raio = raio
    #Método para obter o raio do círculo
    def getRaio(self):
        return self.raio
    
x = int(input("Digite o valor do raio: "))
circulo1 = Circulo(x)
print(circulo1.area())
x = int(input("Digite o novo valor do raio: "))
circulo1.setRaio(x)
print(circulo1.getRaio())
print(circulo1.area())