####################Receba uma matriz quadrada de inteiros e calcule a soma dos elementos das diagonais principal e secundária.####################
#18#
def soma_sec(m):
    soma = 0
    j = len(matriz)
    for i in range(j):
     soma += matriz[i][j - 1 - i]
    return soma

def soma_prin(m):
    soma = 0
    j = len(matriz)
    for i in range(j):
     soma += matriz[i][i]
    return soma

def quad():
    n = int(input("Digite o tomanho da matriz:"))
    matriz = []
    print("Digite os elementos se parado por espaço, sendo linha por linha: \n")

    for i in range(n):
        num = list(map(int, input().split()))
        matriz.append(num)
    return matriz
    
print ("##### Bem vindo a calculadora de diagonais de uma matriz ##### \n")   
matriz = quad()
soma_secundaria = soma_sec(matriz)
soma_primaria = soma_prin(matriz)
print(f"A soma da diagonal secundaria eh: {soma_primaria}")
print(f"A soma da diagonal secundaria eh: {soma_secundaria}")
    


        

