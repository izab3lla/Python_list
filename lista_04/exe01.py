#Escreva uma função recursiva chamada reverter_caracteres(s) que recebe uma
#string s e devolve a string invertida.

def reventer_caracteres(s):
    if s == '':
        return ''
    return reventer_caracteres(s[1:]) + s[0]

s = input('Digite uma palavra:')
resultado = reventer_caracteres(s)

print(resultado)