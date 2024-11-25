#################### Receba uma frase e retorne um dicionário que contém a quantidade de cada caractere (inclusive espaços) ####################
#20#

def fib(n):
    fib_list = []
    a = 0
    b = 1
    for _ in range(n):
        fib_list.append(a)
        a, b = b, a + b
    return fib_list

def num_fb():
    n = int(input("Digite um numero:"))
    fi_seq = fib(n)
    print(f"{fi_seq}")

print ("##### Bem vindo gerador de sequencia de fibonacci! ##### \n")

num_fb()

