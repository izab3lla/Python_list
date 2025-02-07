#Crie uma função que receba uma lista de palavras e retorne a soma total de letras
#em todas as palavras, utilizando map para contar as letras e reduce para somar.

from functools import reduce

def soma_letras(lista8):
    conta_letra = list(map(lambda x: len(x), lista8))
    soma = reduce(lambda x, y: x + y, conta_letra)
    return soma

lista8 = ['iza', 'bella']

resultado = soma_letras(lista8)
print(resultado)
