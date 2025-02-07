#Escreva uma função que receba uma lista de tuplas, onde cada tupla contém
#números inteiros. Utilize map e filter para filtrar as tuplas cuja média dos valores
#seja maior que 5.

def filtrar(lista9):
    #Retorna as médias das tuplas que são maiores que 5.
    media = list(map(lambda x: sum(x) / len(x), lista9))
    maiores = list(filter(lambda x: x > 5, media))
    return maiores


# Exemplo de uso
lista9 = [(3, 2), (5, 6), (8, 7)]
resultado = filtrar(lista9)
print(resultado) 
