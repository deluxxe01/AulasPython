# Você trabalha no setor de Business Intelligence (BI) de uma empresa de
# tecnologia. Sua tarefa é monitorar a produtividade dos funcionários durante o
# mês.
# Crie um programa em Python que:
# Use um laço while para permitir o cadastro de funcionários (nome e setor) até
# que o usuário decida parar (ex: digitando &quot;sair&quot;).
# Para cada funcionário cadastrado, use um laço for para registrar a quantidade
# de tarefas concluídas por semana durante o mês de Setembro (4 semanas).
# Calcule e mostre:
# A média de tarefas por funcionário no mês (len() pode ser usado para contar as
# semanas).
# O total geral de tarefas da equipe no mês.
# Exiba dois gráficos com matplotlib:
# �� Gráfico 1 (linha): mostra a evolução da produtividade da equipe nas 4
# semanas de Setembro (somando tarefas de todos os funcionários por semana).
# �� Gráfico 2 (barras): mostra a produtividade total por funcionário no mês de
# Setembro.
import matplotlib.pyplot as plt

resposta = ""
funcionarios = []
setores=[]
tarefasFuncionarios = []

while resposta != "sair":
    nome = input("Digite o nome do funcionario: ")  
    setor = input("Digite o setor do funcionario: ")
    funcionarios.append(nome)
    setores.append(setor)
    resposta = input("Desejar parar? escreva sair: ")

for i in range(0,len(funcionarios),1):
    semana1 = int(input(f"Funcionario {funcionarios[i]}Digite a quantidade de tarefas concluidas na semana 1: "))
    semana2 = int(input(f"Funcionario {funcionarios[i]}Digite a quantidade de tarefas concluidas na semana 2: "))
    semana3 = int(input(f"Funcionario {funcionarios[i]}Digite a quantidade de tarefas concluidas na semana 3: "))
    semana4 = int(input(f"Funcionario {funcionarios[i]}Digite a quantidade de tarefas concluidas na semana 4: "))
    mediaTarefa = (semana1 + semana2 + semana3 + semana4) / 4
    tarefas = semana1 + semana2 + semana3 + semana4
    tarefasFuncionarios.append(tarefas)

totalGeralEquipe =  sum(tarefasFuncionarios)
print(f"Total de vendas da equipe: {totalGeralEquipe}")