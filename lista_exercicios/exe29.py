####################Receba uma lista de listas (uma lista aninhada)
# com valores duplicados e crie uma nova lista de listas onde cada 
# sublista contenha apenas valores únicos ####################
#29#

def remove_duplicatas(lista):
    lista_final = []

    for i in lista:

        lista_final.append(list(set(i)))

    return lista_final

lista_aninhada = [[1, 1, 2, 3, 3], [4, 5, 5, 6], [7, 7, 8, 9, 9]]

resultado = remove_duplicatas(lista_aninhada)

print(resultado)