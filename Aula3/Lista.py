#REVIW     0, 1, 2, 3, 4
numeros = [1, 2, 3, 4, 5]
#aquarella se inscrever vaga
x = numeros[3] + numeros[2]
print(x) #Resultado: 7

# COMANDOS
numeros.append(6) #Adcionando um valor no final da lista
print(numeros) #Resultado: [1, 2, 3, 4, 5, 6]

numeros.insert(2,7) #Posição, valor adcionado
print(numeros) #Resultado: [1, 2, 7, 3, 4, 5, 6]

numeros.pop(2) #Excluindo um valor na posição
print(numeros) #Resultado: [1, 2, 3, 4, 5, 6]

numeros.insert(6,7) #Posição, valor adcionado
print(numeros) #Resultado: [1, 2, 3, 4, 5, 6, 7]

numeros.remove(7) #Remove o primeiro 7 que ve
print(numeros) #Resultado: [1, 2, 3, 4, 5, 6]

#MÉTODOS
x = numeros.count(2) #Diz quantas vezes tem o valor 2
print(x) #Resultado: 1

y = numeros.index(3) #Diz a posição que ta o primeiro valor 2 
print(y) #Resultado: 2

numerosDois = [7, 11, 9, 10]
numeros.extend(numerosDois) #Colocar os valores do arrey numerosDois dentr do numeros 
print(numeros) #Resultado: [1, 2, 3, 4, 5, 6, 7, 11, 9, 10]

numeros.sort() #Arruma os numeros em ordem CRESCENTE
print(numeros) #Resultado: [1, 2, 3, 4, 5, 6, 7, 9, 10, 11]

numeros.sort(reverse=True) #Arruma os numeros em ordem DECRESCENTE
print(numeros) #Resultado: [11, 10, 9, 7, 6, 5, 4, 3, 2, 1]

numeros.clear() #Excluir os valores que tao dentro do arrey
print(numeros) #Resultado: []

#KEYWORDS
lista = [10, 20, 30, 40, 50]
x = len(lista) #Retorna o tamanho da lista (quantos itens tem)
print(x) #Resultado: 5

y = max(lista) #Retorna o maior elemento da lista
print(y) #Resultado: 50

w = min(lista) #Retorna o menor elemento da lista
print(w) #Resultado: 10

h = sorted(lista) #Retorna a lista ordenada
print(h) #Resultado: [10, 20, 30, 40, 50]

k = list(reversed(lista)) #Retorna a lista invertida como um objeto
print(k) #Resultado: [50, 40, 30, 20, 10]

