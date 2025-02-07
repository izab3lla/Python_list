#Escreva uma função que, utilizando filter e uma função lambda, receba uma lista
#de números inteiros e retorne apenas os números pares.

def numeros_pares(num):
    #Recebe uma lista de números e retorna uma nova lista contendo apenas os números pares.
    num_pares = list(filter(lambda x: x % 2 == 0, num))
    return num_pares


# Exemplo de uso
num = [2, 8, 9, 10, 3, 5, 7]
num_pares = numeros_pares(num)
print(num_pares)
