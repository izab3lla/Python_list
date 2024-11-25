#################### Receba uma palavra e determine se ela é um palíndromo (ou seja, se lê igual de trás para frente). ####################
#14#

def palindromo(palavra):
    return palavra == palavra[::-1]

def verifica(palavra):
    if palindromo(palavra):
        print("eh um palindromo!")
    else:
        print("Nao eh um palindromo!")

print ("##### Bem vindo ao verificador de palindromo ##### \n")

palavra = str(input("Digite uma palavra para saber se ela eh um palindromo: \n"))

verifica(palavra)