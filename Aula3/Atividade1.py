# #EXEMPLO 1
def dobro(numero):
     total = numero * 2
     return total 
numeroValor = int(input("Digite um numero: "))
resultado = dobro(numeroValor)
print("Valor do dobro do numero:", resultado)

#EXEMPLO 2
def classificar_Idade(idade):
     if idade < 12:
         return("Criança")
     elif 12 <= idade < 18:
         return("Adolescente")
     elif 18 <= idade < 60:
         return("Adulto")
     else:
         return("Idoso") 

idadeValor = int(input("Digite sua idade: "))
resultado = classificar_Idade(idadeValor)
print("Você é", resultado)

#EXEMPLO 3
def calcular_media(lista_notas):
    soma = 0 
    for nota in lista_notas:
        soma += nota
    media = soma / len(lista_notas)
    return media

quantidade_alunos = int(input("Digite a quantidade de alunos: "))

for i in range(quantidade_alunos):
    nome = input("Digite o nome do aluno: ")
    notas = []
    for j in range(3):  # Use outro nome que não 'i'
        nota = float(input(f"Digite a nota {j+1}: "))
        notas.append(nota)
    media = calcular_media(notas)  # Agora dentro do loop
    print("Aluno:", nome)
    print("Média:", media)
    if media >= 7:
        print("Aprovado\n")
    else:
        print("Reprovado\n")