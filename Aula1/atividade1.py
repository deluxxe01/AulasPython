# ATIVIDADE 1 (estrutura de condição)
# Descrição: Sistema de Login

# Usuário e senha definidos no código
usuario_correto = "admin"
senha_correta = "1234"

# Solicita os dados ao usuário
usuario_digitado = input("Digite o nome de usuário: ")
senha_digitada = input("Digite a senha: ")

# Verifica se estão corretos
if usuario_digitado == usuario_correto and senha_digitada == senha_correta:
    print("Login efetuado com sucesso.")
else:
    print("Login não efetuado.")
    
# ATIVIDADE 2 (estrutura de condição)
# Descrição: Avaliador de média escolar

nota1 = float(input("Digite a sua primeira nota:"))
nota2 = float(input("Digite a sua segunda nota:"))
nota3 = float(input("Digite a sua terceira nota:"))

media = (nota1 + nota2 + nota3)/3

if media >= 7:
    print("Aprovado!")
elif 5 <= media < 7:
    print("Recuperação!")
else:
    print("Reprovado!")
    
# ATIVIDADE 3 (estrutura de condição)
# Descrção: Calcular o preço do cobustivél
