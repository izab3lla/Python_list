#Escreva uma função que receba uma lista de números inteiros e utilize lambda e
#filter para dividir a lista em números pares e ímpares. Retorne um dicionário com
#duas chaves: "pares" e "ímpares"

def separa(numeros):
    #Separa os números pares e ímpares em duas listas.
    separa_par = list(filter(lambda x: x % 2 == 0, numeros))
    separa_impar = list(filter(lambda x: x % 2 != 0, numeros))
    return separa_par, separa_impar

# Exemplo de uso
numeros = [3, 5, 2, 6, 7, 13, 20]
separa_par, separa_impar = separa(numeros)

print(f"Ímpares: {separa_impar} / Pares: {separa_par}")
