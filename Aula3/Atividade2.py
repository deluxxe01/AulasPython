quantNumeros = int(input("Digite a quantidade de numeros que deseja colocar no array: "))
lista = []
for i in range (quantNumeros):
    numero = int(input("Digite o valor: "))
    lista.append(numero)
def analiseLista(lista):
    print(lista)
    lista.sort() #Arruma em ordem crescente
    print(lista)
    lista.sort(reverse=True) #Arruma em ordem decrescente
    print(lista)
    lista.pop(0) #Deleta o primeiro numero
    print(lista)
    lista.pop() #Deleta o ultimo
    print(lista)
analiseLista(lista)