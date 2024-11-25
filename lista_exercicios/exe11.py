#################### Peça ao usuário uma frase e, em seguida, conte quantas palavras únicas ela possui (sem considerar maiúsculas e minúsculas). ####################
#11#

def palavra_unica(palavras):
    palavras = palavras.lower()
    frase = palavra.split()
    palavras_unicas = set(frase)
    return len(palavras_unicas)

print ("##### Bem vindo ao contador de palavras unicas! ##### \n")

palavra = str(input("Insira uma frase: \n"))
quantidade = palavra_unica(palavra)

print(f"A {palavra} possui {quantidade} palavras unicas")
    