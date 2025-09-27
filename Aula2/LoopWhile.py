#EXEMPLO 1
# Colocando valor na variavél
valor = 0

#Enquanto valor for menor que 5 ele vai rodar o loop e somar +1 a cada valor
while valor < 5:
     print(valor)
     valor = valor + 1

#EXEMPLO 2
#Colocando valor na variavél
x = 0

while x < 5:
    print("O valor de x nesta interação é:", x)
    print("X ainda é menor que 5, somando +1 ao X")
    x += 1
else:
    print(x, "Loop Concluído")


# EXEMPLO 3
i = 1
while True:
     print(i)
     i = i + 1
     if i > 3:
       break
     
# EXEMPLO 4
tempoAgora = input("Digite o tempo (sol, chuva, nublado): ")

match tempoAgora:
    case "sol":
        print("Está ensolarado! Use protetor solar.")
    case "chuva":
        print("Está chovendo! Leve um guarda-chuva.")
    case "nublado":
        print("O céu está nublado! Pode chover.")
    case _:
        print("Tempo desconhecido.")