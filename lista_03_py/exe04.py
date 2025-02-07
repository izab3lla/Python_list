#Escreva uma função que receba uma lista de nomes e, utilizando filter, retorne
#apenas os nomes com mais de 5 letras.

def conta_caracter(nomes):
    #Retorna os nomes com 5 ou mais caracteres.
    nomes_cinco = list(filter(lambda x: len(x) >= 5, nomes))
    return nomes_cinco

# Exemplo de uso
nomes = ["Julia", "Guilherme", "Ana", "Maria", "Nina", "Judite"]
nomes_cinco = conta_caracter(nomes)
print(nomes_cinco) 
