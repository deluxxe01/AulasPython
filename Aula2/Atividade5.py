import matplotlib.pyplot as plt

resposta = ""
funcionarios = []
setores = []
tarefasFuncionarios = []  # Tarefas totais por funcionário
tarefasSemanaisEquipe = [0, 0, 0, 0]  # Soma de tarefas da equipe por semana

# Cadastro de funcionários
while True:
    nome = input("Digite o nome do funcionário (ou 'sair' para encerrar): ").strip()
    if nome.lower() == "sair":
        break
    setor = input("Digite o setor do funcionário: ").strip()
    funcionarios.append(nome)
    setores.append(setor)

# Registro das tarefas
for i in range(len(funcionarios)):
    print(f"\nRegistro de tarefas para {funcionarios[i]}:")
    tarefasFuncionario = []
    for semana in range(4):
        tarefas = int(input(f"  Semana {semana + 1}: "))
        tarefasFuncionario.append(tarefas)
        tarefasSemanaisEquipe[semana] += tarefas
    total = sum(tarefasFuncionario)
    media = total / len(tarefasFuncionario)
    tarefasFuncionarios.append(total)
    print(f"  Média de tarefas no mês: {media:.2f}")

# Total geral da equipe
totalGeralEquipe = sum(tarefasFuncionarios)
print(f"\n🔹 Total de tarefas da equipe em Setembro: {totalGeralEquipe}")

# Gráfico 1: Evolução semanal da equipe
plt.figure(figsize=(10, 5))
plt.plot(range(1, 5), tarefasSemanaisEquipe, marker='o', linestyle='-', color='blue')
plt.title('Produtividade Semanal da Equipe - Setembro')
plt.xlabel('Semana')
plt.ylabel('Total de Tarefas')
plt.xticks([1, 2, 3, 4])
plt.grid(True)
plt.tight_layout()
plt.show()

# Gráfico 2: Produtividade por funcionário
plt.figure(figsize=(10, 5))
plt.bar(funcionarios, tarefasFuncionarios, color='green')
plt.title('Produtividade Total por Funcionário - Setembro')
plt.xlabel('Funcionário')
plt.ylabel('Tarefas Concluídas')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()