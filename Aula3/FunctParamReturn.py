#Função com parâmetro e return
def par_impar(numero):
     if numero % 2 == 0:
         return ("par")
     else: 
         return ("impar")
    
numeroValor = int(input("Digite um numero: "))
resultado = par_impar(numeroValor)
print("Resultado: ", resultado)

#EXEMPLO 5
def calcular_area(largura,comprimento):
    area = largura * comprimento
    return area
larguraValor = float(input("Digite o valor da largura: "))
comprimentoValor = float(input("Digite o valor do comprimento: "))
precoMetroQuadrado = float(input("Digite o valor por metro quadrado: "))

areaImovel = calcular_area(larguraValor, comprimentoValor)
precoImovel = areaImovel * precoMetroQuadrado
print("Preço do imovel sera: ", precoImovel)