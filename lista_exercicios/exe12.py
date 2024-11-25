#################### Peça ao usuário uma frase e, em seguida, conte quantas palavras únicas ela possui (sem considerar maiúsculas e minúsculas). ####################
#12#

def eh_primo(num):
    for n in range(2, num):
        if num %n == 0:
            return False
    return True

def intervalo(inicio, fim):
    numeros=[]
    for i in range (inicio, fim):
        if eh_primo(i):
            numeros.append(i)
    return numeros

print ("##### Bem vindo ao gerador de intervalo de numeros primos! ##### \n")

inicio = int(input("Digite o numero que deseja começar seu intervalo de numeros primos:"))
fim = int(input("Digite o numero que deseja que se encerre o intervalo:"))

primos = intervalo(inicio, fim)

print(primos)