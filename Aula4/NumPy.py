import numpy as np
import math
import time

precos_np = np.random.rand(10_000_000)
type(precos_np)
precos_np

#Criar uma lista de Python Puro
precos_list = list(precos_np)
type(precos_list)
precos_list

#Operação com NumPy
t0 = time.time()
desc = precos_np * 0.9
final = desc + 5
raiz = np.sqrt(precos_np)
print("Numpy: ", time.time()-t0, "segundos")

#Operação com Python puro
t0 = time.time()
desc = [p * 0.9 for p in precos_list]
final = [p + 5 for p in desc]
raiz = [math.sqrt(p) for p in precos_list]
print("Python puro: ", time.time() - t0, "segundos")

#Criando um array de 1 dimensão (vetor) a partir de uma lista de Python 
vetor = np.array([17, 21, 100, 34])
print("\nVetor array 1D: \n")
print(vetor)

#Verificando atributos
print("Formato(shape) do vetor:", vetor.shape)
print("Número de dimensões(ndim) do vetor:", vetor.ndim)
print("Número total de elementos(size) do vetor:", vetor.size)

#Criando um array de 2 dimensões (matriz) a partir de uma lista de listas
duasDimensoes = np.array([[1, 2, 3], [4, 5, 6]])
print("Matriz com 2D:")
print(duasDimensoes)

#Verificando atributos
print("Formato(shape) do vetor:", duasDimensoes.shape)
print("Número de dimensões(ndim) do vetor:", duasDimensoes.ndim)
print("Número total de elementos(size) do vetor:", duasDimensoes.size)

#Criando um array 3Dimensoes usando np.arange()
tresDimensoes= np.arange(24).reshape(4, 3, 2)
print("\nArray de 3D:")
print(tresDimensoes)

#Verificando atributos
print("Formato(shape) do vetor:", tresDimensoes.shape)
print("Número de dimensões(ndim) do vetor:", tresDimensoes.ndim)
print("Número total de elementos(size) do vetor:", tresDimensoes.size)

#NumPy interfere o tipo de dado automaticamente
arr_inteiros = np.array([1, 2, 3, 4])
print("Tipo de dado (int):", arr_inteiros.dtype)

#Podemos especificar o tipo de dado durante a criação
arr_float = np.array([1, 2, 3, 4], dtype= np.float64)
print("Tipo de dado float64:", arr_float.dtype)
print("Array float:", arr_float)

#Conversão para inteiro
arr_int = arr_float.astype(np.int64)
print("Tipo convertido:", arr_int.dtype)
print("Array convertido:", arr_int)

#Criando uma matriz 4x4 com numeros de 0 a 15
dados = np.arange(16).reshape(4, 4)
print("Matriz:\n", dados)

#Resultado Matriz:
#   0  1  2  3
#0 [[ 0  1  2  3]
#1 [ 4  5  6  7]
#2 [ 8  9 10 11]
#3 [12 13 14 15]]

#Acessando um elemento específico: linha 1, coluna 2
elemento = dados[1, 2]
print("Matriz:\n", {elemento})
