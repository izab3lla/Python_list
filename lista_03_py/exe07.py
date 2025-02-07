#Escreva uma função que receba uma lista de números inteiros e utilize map e filter
#para criar um dicionário que agrupe os números em três categorias:

def tres_categorias(numeros):
    #Separa os números em três categorias: iguais a zero, positivos e negativos.
    # Lista com números iguais a zero
    iguais_zero = list(filter(lambda x: x == 0, numeros))
    
    # Lista com números positivos
    positivos = list(filter(lambda x: x > 0, numeros))
    
    # Lista com números negativos
    negativos = list(filter(lambda x: x < 0, numeros))
    
    return iguais_zero, positivos, negativos

# Lista de exemplo
numeros = [3, -5, 2, 6, 0, 78, 1, -10]

iguais_zero, positivos, negativos = tres_categorias(numeros)
print(f"Números positivos: {positivos} / Números negativos: {negativos} / Iguais a zero: {iguais_zero}")

