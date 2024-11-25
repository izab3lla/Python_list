#################### Solicite uma palavra do usuário e exiba quantos caracteres ela possui ####################
#04#

def contador(palavra):
    return len(palavra)

print ("##### Bem vindo ao contador de palavras ##### \n")
letra = str(input("Escreva a palavra que deseja saber quantos caracteres possui: \n"))
num = contador(letra)

print(f"A palavra {letra} possui {num} caracteres")
