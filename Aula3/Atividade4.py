#ENCAPSULAMENTO privados e públicos 
       # self._saldo = 0.0 #Atributo privado (com_)
       # self._nome = nome #Atributo privado (com_)

#Herança
class Automovel:
    def __init__(self, marca, modelo):
        self.marca = marca
        self. modelo = modelo

    def imprimir_dados(self):
        print(self.marca, self.modelo)
        
class Carro(Automovel):
    def __init__(self,marca, modelo, num_portas):
        super(). __init__(marca,modelo)
        self.num_portas = num_portas

class Moto(Automovel):
    def __init__(self, marca, modelo, estilo):
        super(). __init__(marca,modelo)
        self.estilo = estilo

fusca = Carro("Volkswagen", "Fusca", 2)
fusca.imprimir_dados()
print(fusca.num_portas)

biz = Moto("Honda", "XRl", "Malizada")
biz.imprimir_dados()
print(biz.estilo)

