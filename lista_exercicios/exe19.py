#################### Receba uma frase e retorne um dicionário que contém a quantidade de cada caractere (inclusive espaços) ####################
#19#

def num_carac(frase):
    cont = {}
    for carac in frase:
        if carac in cont:
            cont[carac] += 1
        else:
            cont[carac] = 1
    return cont

print ("##### Bem vindo contador de caracter em uma frase ##### \n")
frase = str(input("Digite uma frase:"))

resultado = num_carac(frase)

for carac, qant in resultado.items():
    print(f"o caracter {carac} aparece {qant} vezes")