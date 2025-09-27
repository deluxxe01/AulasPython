validador = "sair"
produtos = []
total = 0
media_semanal = 0 

while validador != "sair":
     nomeProduto = input("Digite o nome do produto: ")
     produtos.append(nomeProduto)
     validador = input("Deseja parar? escreva (Sair): ")


for i in range(len(produtos)):
     for i in range(0,4,1):
          quant_recb_semana = int(input(f"Digite quanto recebeu na {i + 1} semana: "))
          total += quant_recb_semana
          media_semanal = total / len(produtos) if len(produtos) > 0 else 0
          

# Dados do gráfico

