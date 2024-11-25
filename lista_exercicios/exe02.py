####################  Peça ao usuário um número inteiro e informe se ele é par ou ímpar ####################
#02#

def impar_par(a):
    if  a %2 == 0:
        print("O numero eh par!")
    else: 
        print("O numero eh impar!")

print ("##### Escolha um numero que diirei se eh impar ou par! ##### \n")
a = int(input("insira um numero: \n"))

impar_par(a)