####################Receba uma lista de inteiros e filtre apenas os números pares. ####################
#25#
def filtro(lista):
    nova_lista = []
    for i in lista:
        if i %2 == 0:
            nova_lista.append(i)
    return nova_lista

print ("##### Bem vindo ao filtrador de numeros pares!! ##### \n")

lista = list(map (int, input("Digite uma lista de numero separando pr espacos:").split()))

resultado = filtro(lista)
print(resultado)