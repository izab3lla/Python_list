####################Peça ao usuário dois números e uma operação (adição, subtração, multiplicação ou divisão) e execute a operação escolhida.####################
#23#

def calc(n1, n2):
    op = input("Escolha uma das operacoes (+, -, *, /)")

    if op == "+" :
        soma = n1 + n2
        print ("A soma eh:", soma)

    elif op == "-" :
        soma = n1 - n2
        print ("A soma eh:", soma)

    elif op == "*":
        soma = n1 * n2
        print ("a multiplicacao eh:", soma)

    elif op == "/":
         soma = n1 / n2
         print ("a divisao eh:", soma)

print ("##### Bem vindo a calculadora em python!! ##### \n")

n1 = int(input ("Digite o primeiro numero:"))
n2 = int(input("Digite o segundo numero:"))


calc(n1, n2)
    