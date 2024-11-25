#################### Peça a idade do usuário e informe se ele é maior de idade (18 anos ou mais) ou menor de idade. ####################
#09#

def maior_menor():
    idade = int(input("Informe a idade do usuario:"))
    if idade >= 18:
        print ("Usuario maior de idade!")
    else:
        print("Usuario menor de idade!")

print ("##### Bem vindo ao verificador de maioridade!!##### \n")

maior_menor()
