validador = ""
produtos = []
total_semana = []
soma = 0

while validador != "sair":
     nomeProduto = input("Digite o nome do produto: ")
     produtos.append(nomeProduto)
     validador = input("Deseja parar? escreva (Sair): ")


for i in range(len(produtos)):
     for i in range(0,4,1):
          quant_recb_semana = int(input(f"Digite quanto recebeu na {i + 1} semana para {nomeProduto}: "))
          soma += quant_recb_semana
          total_semana[i] += quant_recb_semana
         
media = soma / 4


