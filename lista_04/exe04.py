#Escreva uma função recursiva chamada indice_maior_elemento(lista) que retorna o
#índice do maior elemento em uma lista

lista = [4, 5, 7, 2, 3]

def indice_maior_elemento(lista, indice = 0, maior_indice = 0):
    if indice == len(lista):
        return maior_indice
    
    if lista[indice] > lista[maior_indice]:
        maior_indice = indice
    return indice_maior_elemento(lista, indice + 1, maior_indice)

resultado = indice_maior_elemento(lista)
print(resultado)


