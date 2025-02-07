#Escreva uma função que, utilizando map e uma função lambda, receba uma lista
#de números inteiros e retorne uma nova lista com todos os elementos dobrados.


def dobro_numero(num):
    #Recebe uma lista de números e retorna uma nova lista com o dobro de cada número.
    dobro = list(map(lambda x: x * 2, num))
    return dobro


# Exemplo de uso
num = [2, 4, 3, 8]
dobro = dobro_numero(num)
print(dobro)
