#################### Dada uma lista de números, exiba quantos números ela contém ####################
#08#
import random

def qant_lista(num):
    return [random.randint(1,15) for _ in range(num)]

def quantidade(q):
    quant = len(q)
    return quant

print ("##### Bem vindo ao contador de numeros ##### \n")

numero = qant_lista(10)

quantidade(numero)
 