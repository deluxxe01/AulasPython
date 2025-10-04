import matplotlib.pyplot as plt

disciplina = []
nomes = []

quantAlunos = int(input("Digite a quantidade de alunos: "))

# 1. Coletar as notas e nomes
for i in range(quantAlunos):
    nome = input(f"\nDigite o nome do aluno {i + 1}: ")
    nota = float(input(f"Digite a nota do aluno {nome}: "))
    nomes.append(nome)
    disciplina.append(nota)

# 2. Calcular a média geral
media = sum(disciplina) / len(disciplina)
print(f"\nMédia geral da turma: {media:.2f}")

# 3. Contar alunos acima/abaixo da média
acima = 0
abaixo = 0

for i in range(quantAlunos):
    if disciplina[i] >= media:
        print(f"{nomes[i]} está ACIMA da média")
        acima += 1
    else:
        print(f"{nomes[i]} está ABAIXO da média")
        abaixo += 1

print(f"\nTotal de alunos acima da média: {acima}")
print(f"Total de alunos abaixo da média: {abaixo}")

# 4. Gráfico de distribuição das notas
plt.figure(figsize=(10, 5))
plt.bar(nomes, disciplina, color='mediumslateblue')
plt.axhline(media, color='red', linestyle='--', label=f'Média ({media:.2f})')
plt.title('Distribuição das Notas dos Alunos')
plt.xlabel('Alunos')
plt.ylabel('Nota')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
