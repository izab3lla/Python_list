#Crie uma função que, utilizando reduce e uma função lambda, receba uma lista de
#números inteiros e retorne a soma total dos números.
from functools import reduce

def soma_numeros(num):
    #Retorna a soma de todos os números da lista.
    soma_total = reduce(lambda x, y: x + y, num)
    return soma_total

# Exemplo de uso
num = [4, 3, 2, 5, 7, 6]
soma_total = soma_numeros
