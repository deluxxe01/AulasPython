import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#1. Exemplo simples para testar
num_usuarios = 500
visitas = np.random.randint(1, 51, size=num_usuarios)
#print(visitas)

#2. gerar o tempo no site (distribuindo normal, correlacionando com visitas)
# média de 20min, desvio padrão de 5, com um bônus por visita
time_on_site = np.random.normal(loc=20, scale=5, size=num_usuarios) + visitas * 0.5
time_on_site = np.round(time_on_site, 2)

#3. gerar o numero de item no carrinho (depende de visitas e tempo)
# usuários que visitam mais e passam mais tempo, tendem adicionar mais itens
items_on_cart = np.random.randint(0, 8, size=num_usuarios) + (visitas // 10)

#Garante que o tempo no site também influencie positivamente 
items_on_cart = (items_on_cart + (time_on_site // 15)).astype(int)
print(items_on_cart)


#4. Gerar o valor da compra
buy_value = (items_on_cart * 35) + np.random.normal(loc=0, scale=5, size=num_usuarios) + visitas * 0.5

#Se não houver itens no carrinho, o valor da compra deve ser 0
buy_value[items_on_cart == 0] = 0
buy_value[buy_value < 0] = 0  # corrigir valores negativos
buy_value = np.round(buy_value, 2)

#Unindo tudo em uma unica matriz(ndarray)
#cada linha representa um usuário, cada coluna uma métrica
dados_ecommerce = np.column_stack((visitas, time_on_site, items_on_cart, buy_value))

print("\nShape da nossa massa de dados:", dados_ecommerce.shape)
print("\nExemplo dos primeiros 5 usuários linha: ")
print(dados_ecommerce[:5])

# Separando as colunas para facilitar a leitura do código
visitas_col = dados_ecommerce[:, 0]
tempo_col = dados_ecommerce[:, 1]
itens_col = dados_ecommerce[:, 2]
valor_col = dados_ecommerce[:, 3]

print("--- ANÁLISE ESTATÍSTICA GERAL ---")

# Média
media_visitas = np.mean(visitas_col)
media_tempo = np.mean(tempo_col)
media_itens = np.mean(itens_col)
media_valor = np.mean(valor_col)

print(f"\nMédia de Visitas: {media_visitas:.2f}")
print(f"Média de Tempo no Site: {media_tempo:.2f} min")
print(f"Média de Itens no Carrinho: {media_itens:.2f}")
print(f"Média de Valor de Compra (Ticket Médio): R$ {media_valor:.2f}")

# Mediana (valor central, menos sensível a outliers)
mediana_valor = np.median(valor_col)
print(f"\nMediana do Valor de Compra: R$ {mediana_valor:.2f}")

# Desvio Padrão (mede a dispersão dos dados)
std_valor = np.std(valor_col)
print(f"Desvio Padrão do Valor de Compra: R$ {std_valor:.2f}")

# Valores Máximos e Mínimos
max_valor = np.max(valor_col)
min_valor_positivo = np.min(valor_col[valor_col > 0])  # Mínimo apenas entre quem comprou
print(f"Maior Valor de Compra: R$ {max_valor:.2f}")
print(f"Menor Valor de Compra (de quem comprou): R$ {min_valor_positivo:.2f}")

# Filtro booleano para clientes com compras > R$ 250
clientes_alto_valor = dados_ecommerce[dados_ecommerce[:, 3] > 250]

print("\n--- ANÁLISE: CLIENTES DE ALTO VALOR (Compras > R$ 250) ---\n")
print(f"Número de clientes de alto valor: {clientes_alto_valor.shape[0]}")

# Estatísticas deste segmento
media_visitas_alto_valor = np.mean(clientes_alto_valor[:, 0])
media_tempo_alto_valor = np.mean(clientes_alto_valor[:, 1])

print(f"Média de visitas desses clientes: {media_visitas_alto_valor:.2f}")
print(f"Média de tempo no site desses clientes: {media_tempo_alto_valor:.2f} min")

# Filtro quem não comprou
visitantes_sem_compra = dados_ecommerce[dados_ecommerce[:, 3] == 0]

print("\n--- ANÁLISE: VISITANTES QUE NÃO COMPRAM ---\n")
print(f"Número de visitantes que não compraram: {visitantes_sem_compra.shape[0]}")

# Estatísticas deste segmento
media_tempo_sem_compra = np.mean(visitantes_sem_compra[:, 1])
media_visitas_sem_compra = np.mean(visitantes_sem_compra[:, 0])

print(f"Média de visitas desses visitantes: {media_visitas_sem_compra:.2f}")
print(f"Apesar de não comprarem, eles passam em média {media_tempo_sem_compra:.2f} min no site.")


# --- GRÁFICO ---
plt.figure(figsize=(12, 5))
plt.hist(valor_col, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
plt.axvline(media_valor, color='red', linestyle='--', linewidth=2, label=f'Média = R$ {media_valor:.2f}')
plt.axvline(mediana_valor, color='orange', linestyle='--', linewidth=2, label=f'Mediana = R$ {mediana_valor:.2f}')
plt.axvline(media_valor + std_valor, color='green', linestyle=':', linewidth=2, label=f'+1 DP = R$ {media_valor + std_valor:.2f}')
plt.axvline(media_valor - std_valor, color='green', linestyle=':', linewidth=2, label=f'-1 DP = R$ {media_valor - std_valor:.2f}')
plt.title('Distribuição dos Valores de Compra')
plt.xlabel('Valor da Compra (R$)')
plt.ylabel('Frequência')
plt.legend()
plt.grid(alpha=0.3)
plt.show()


# Calcula a matriz de correlação
matriz_correlacao = np.corrcoef(dados_ecommerce, rowvar = False)


# Define os nomes das variáveis
nomes_variaveis = ["Visitas", "Tempo no Site", "Itens no Carrinho", "Valor da Compra"]


# Converte em DataFrame para exibir com rótulos
df_correlacao = pd.DataFrame(matriz_correlacao,
                             index = nomes_variaveis,
                             columns = nomes_variaveis)


# Matriz de correlação (mapa de calor)
plt.figure(figsize = (7, 5))
sns.heatmap(df_correlacao, annot = True, cmap = "Blues", fmt = ".2f")
plt.title("Matriz de Correlação")
plt.show()