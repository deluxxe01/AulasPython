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
objeto_pessoa1.imprimirDados()
objeto_pessoa2.imprimirDados()
objeto_pessoa3.imprimirDados()