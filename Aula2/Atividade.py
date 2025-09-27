#ATIVIDADE 1 
#Descrição: você tem as vendas de um vendedor durante 12 messes
# . a meta mensal é 10.000. Para cada mês, informe se a meta foi alcançada
metas = 10000
metasBatida = 0
vendas = []

# Coleta de vendas
for i in range(12):
    valor = float(input(f"Digite o valor de vendas no mês {i + 1}: "))
    vendas.append(valor)

# Verificação de metas
for i in range(12):
    if vendas[i] >= metas:
        metasBatida += 1

# Resultado
print("Quantidade de metas batidas:", metasBatida)