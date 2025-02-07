#Crie uma função que eleve ao quadrado todos os números de uma lista, utilizando
#map, e depois retorne a lista ordenada.

def quadrado(num):
    #Retorna uma lista com o quadrado de cada número.
    quad = list(map(lambda x: x ** 2, num))
    return quad

# Exemplo de uso
num = [3, 5, 2, 7, 6]
quad = quadrado(num)
ordenadas = sorted(quad)

print(ordenadas)
