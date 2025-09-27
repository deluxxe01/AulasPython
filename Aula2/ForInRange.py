# EXEMPLO FOR IN RANGE
#Crie a variavel i que começa com 20
# Traduzir: Não pare conforme: (start, stop, step)
for i in range(20, 100, 5):
    print(i)

for i in range(20, 100,5):
    if(i % 2 == 0):
        print(i)

# EXEMPLO FOR IN RANGE
gastos = [150,120,130,110]
total = 0 

for i in range(0,4,1):
   print(f"Abastecimento {i + 1}: R${gastos[i]:.2f}")
   total = total + gastos[i]

   media = total / 4
   print(f"\nTotal: R${total:.2F}")
   print(f"Media: R${media:.2f}")


# EXEMPLO FOR IN RANGE 
abst1 = float(input("Digite o primeiro abastecimento: "))
abst2 = float(input("Digite o segundo abastecimento: "))
abst3 = float(input("Digite o terceiro abastecimento: "))
abst4 = float(input("Digite o quarto abastecimento: "))

gastos = [abst1, abst2, abst3, abst4]
total = 0 

for i in range(0,4,1):
   print(f"Abastecimento {i + 1}: R${gastos[i]:.2f}")
   total = total + gastos[i]

   media = total / 4
   print(f"\nTotal: R${total:.2f}")
   print(f"Media: R${media:.2f}")

# EXEMPLO FOR IN COM VETOR
fruta1 = input("Digite a primeira fruta: ")
fruta2 = input("Digite a segunda fruta: ")
fruta3 = input("Digite a terceira fruta: ")

# Posição das frutas: 0,1,2
listaFrutas = [fruta1, fruta2, fruta3]
for i in range(0,3,1):
    print(listaFrutas[i])

#Essa parte ja nao faz parte do loop
print("Programa finalizado!")


# EXEMPLO FOR IN COM VETOR
SacolaFrutas = []
for i in range(0,3,1):
     fruta = input("Digite uma fruta da feira: ")
     SacolaFrutas.append(fruta)
print("Frutas adcionadas com sucesso na sacola!")

for i in range(0,3,1):
     print(SacolaFrutas[i])
print("Sacola de frutas finalizado!")

# EXEMPLO USANDO DECRESCENTE 5,4,3,2,1
contagemRegressiva = int(input("Digite o numero da contagem: "))
for i in range(contagemRegressiva,0, -1):
     print(i)
print("Contagem finalizada!")

# EXEMPLO USANDO RANGE E IF 
# Você deverá realizar um programa que irá mostrar todos os números ímparas entre 0 e 100 
for i in range(0,101,1):
     if (i % 2 != 0):
         print(i)
print("Programa finalizado!")

# EXEMPLO USANDO WHILE E FOR 
x = "sim"
listaFruta = []
while x == "sim":
    fruta = input("Digite a fruta: ")
    listaFruta.append(fruta)
    x = input("Você quer continuar?")

for i in range(0,len(listaFruta),1):
    print(listaFruta[i])
print("Finish de frutas! :)")