#################### Implemente um jogo onde o programa escolhe um número aleatório entre 1 e 100, e o usuário deve adivinhar. 
# Após cada tentativa, diga se o número é maior ou menor que o 
# número secreto, e conte o número de tentativas até acertar. ####################
#15#
import random

def gerar_num():
    return random.randint(1, 100)

def jogo():
    num_secret = gerar_num()
    tent = 0

    while True:
        tent += 1
        chute = int(input("Digite o seu palpite:"))

        if chute > num_secret:
            print("O numero secreto eh menor")
        elif chute < num_secret:
            print("O numero secreto eh maior")
        else:
            print(f"Acertou! acertou em {tent}")
            break
    
print ("##### Bem vindo ao jogo de adivinhacao ##### \n")
print("Pensei em um numero, tente adivinhar!")
jogo()