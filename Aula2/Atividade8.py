# Objetivo: Criar um sistema simples de controle de estoque de um
# supermercado. O programa deve perguntar o nome e a quantidade de 5
# produtos no estoque, e depois mostrar se algum produto está abaixo do
# estoque mínimo (definido pelo usuário) e mostrar um gráfico com o estoque
# atual de cada produto.
#  Estruturas usadas: Laços de repetição (for), estrutura de condição
# (if/else), vetor/array, gráficos.
# Passos:
# 1. Perguntar o nome e a quantidade de 5 produtos.
# 2. Perguntar o estoque mínimo.
# 3. Verificar se algum produto está abaixo do estoque mínimo e imprimir um
# alerta.
# 4. Plotar um gráfico de barras com o estoque de cada produto.

quantProdutos = 5

for i in range(quantProdutos):
    nome = input(f"\nDigite o nome do produto {i + 1}: ")
    setor = input(f"\nDigite o nome do setor {i +1}: ")
