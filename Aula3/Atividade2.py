quantNumeros = int(input("Digite a quantidade de numeros que deseja colocar no array: "))
lista = []
for i in range (quantNumeros):

    numero = int(input("Digite o valor: "))
    lista.append(numero)

def analiseLista(lista):
    print(lista)

    lista.sort() #Arruma em ordem crescente Resultado: [1, 2, 3, 4, 5]
    print(lista)

    lista.sort(reverse=True) #Arruma em ordem decrescente Resultado: [5, 4, 3, 2, 1]
    print(lista)

    lista.pop(0) #Deleta o primeiro numero Resultado: [4, 3, 2, 1]
    print(lista)

    lista.pop() #Deleta o ultimo numero Resultado: [4, 3, 2]
    print(lista)

analiseLista(lista)