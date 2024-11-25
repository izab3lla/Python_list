#################### Peca ao usuario um numero inteiro e informe se ele eh par ou impar ####################
#03#

def temp(t):
    return t * 1.8 + 32

print ("##### Bem vindo ao conversor de temperatura! ##### \n")
temperatura = float(input("Insira uma temperatura: \n"))
conver = temp(temperatura)

print(f"A {temperatura} em Fahrenheit eh: {conver}")

