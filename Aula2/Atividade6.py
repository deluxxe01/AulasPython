# Criar um programa que leia as temperaturas diárias de uma semana (7 dias) e
# calcule a média das temperaturas, além de verificar se algum dia foi mais
# quente ou mais frio que a média. O programa também deve mostrar um gráfico
# com as temperaturas diárias.
#  Estruturas usadas: Laços de repetição (for ou while), estrutura de
# condição (if/else), vetor/array, gráficos.
# Passos:
# 1. O programa deve receber 7 entradas de temperatura para cada dia da
# semana.
# 2. Calcular a média das temperaturas.
# 3. Verificar quantos dias foram acima ou abaixo da média.
# 4. Plotar um gráfico de barras com as temperaturas diárias.


import matplotlib.pyplot as plt

dias_semana = ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb']
temperaturas = []

# 1. Entrada das temperaturas
for i in range(len(dias_semana)):
    temp = float(input(f"Digite a temperatura de {dias_semana[i]}: "))
    temperaturas.append(temp)

# 2. Calcular a média
media = sum(temperaturas) / len(temperaturas)
print(f"\nMédia da semana: {media:.2f}°C")

# 3. Verificar dias acima/abaixo da média
acima = 0
abaixo = 0

for temp in temperaturas:
    if temp > media:
        acima += 1
    elif temp < media:
        abaixo += 1

print(f"Dias acima da média: {acima}")
print(f"Dias abaixo da média: {abaixo}")

# 4. Gráfico de barras
plt.figure(figsize=(8, 5))
plt.bar(dias_semana, temperaturas, color='skyblue')
plt.axhline(media, color='red', linestyle='--', label=f'Média ({media:.2f}°C)')
plt.title('Temperaturas Diárias da Semana')
plt.xlabel('Dia da Semana')
plt.ylabel('Temperatura (°C)')
plt.legend()
plt.tight_layout()
plt.show()
