#Exercício 3: Contar Caracteres em uma String
#Crie uma função recursiva chamada contar_caracteres(s, c) que conta quantas vezes o
#caractere c aparece na string s.

def contar_caracter(s, c):

    if s == '':
        return 0
    if s[0] == c:
        return 1 + contar_caracter(s[1:], c)
    
    return contar_caracter(s[1:], c)
    
st = input('Digite uma palavra: \n')
carac = input("Digite o caractere a ser contado: ")
    
resultado = contar_caracter(st, carac)

print(resultado)
