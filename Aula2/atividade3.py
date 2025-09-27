#Descrição: Você é programador de uma loja de departamento Americanas. Faça um programa qe peça para incluir nome de vendedores
#até quantidade que o usuário não quiser mais. após isso, o programa deve habilitar solicitação da venda do m~es de março dos 
#vendedores. com isso você deve tirar a média do mês de março sendo que deve ter um gráfico mostrando resultado do mês janeiro(vendeu 50mil)
# e fevereiro(vendeu 30mil), oviamente informando tambem março no grafic. por fim mostrar em outro grafico as vendas dos vendedores
import matplotlib.pyplot as plt

vendedores = []
vendas_marco = []
total = 0

x = "sim"
while x.lower() == "sim":
    vendedor = input("Digite o nome do vendedor: ")
    vendedores.append(vendedor)
    x = input("Deseja continuar? (sim/não) ").strip().lower()

for i in range(len(vendedores)):
    venda = float(input(f"Digite quanto o vendedor {vendedores[i]} vendeu em março? R$ "))
    vendas_marco.append(venda)

# Calcula o total de vendas em março
total = sum(vendas_marco)

# Calcula a média
mediaMarco = total / len(vendedores) if len(vendedores) > 0 else 0

# Dados para gráfico de vendas mensais
meses = ["Janeiro", "Fevereiro", "Março"]
valores = [50000, 30000, mediaMarco]

# Gráfico de linhas para vendas mensais
plt.figure(figsize=(8,5))
plt.plot(meses, valores, marker='o', linestyle='--', color='green')
plt.title("Vendas Mensais")
plt.ylabel("Valor vendido (R$)")
plt.grid(True, linestyle='--', alpha=0.6)

# Gráfico de barras para vendas dos vendedores em março
plt.figure(figsize=(10,6))
plt.bar(vendedores, vendas_marco, color='pink')
plt.title("Vendas dos Vendedores em Março")
plt.xlabel("Vendedores")
plt.ylabel("Valor vendido (R$)")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()
