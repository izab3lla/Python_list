####################Receba uma lista de inteiros e retorne uma nova lista sem elementos duplicados, mantendo a ordem original. ####################
#21#

def num(lista):
    nova_lista = []
    for i in lista:
        if i not in nova_lista:
            nova_lista.append(i)
    return nova_lista

print ("##### Bem vindo ao removedor de elementos duplicados!! ##### \n")
elementos = list(map(int, input("Digite uma lista de numeros mantendo um espaco enntra cada um:").split()))

final = num(elementos)

print(final)