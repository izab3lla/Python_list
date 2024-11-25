#################### Peça ao usuário uma frase e conte o número de vogais e consoantes. Ignore espaços e caracteres especiais. ####################
#22#

def num_vogais_consoantes(frase):
    vogais = ["a", "e", "i", "o", "u"]
    consoantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n",
                   "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    frase = frase.lower()
    cont_vogais = 0
    cont_consoantes = 0

    for carac in frase:
        if carac in vogais:
            cont_vogais += 1
        elif carac in consoantes:
            cont_consoantes += 1
    return cont_consoantes, cont_vogais

print ("##### Bem vindo ao contador de vogais e consoantes!! ##### \n")

frase = str(input("Digite uma frase:"))
vogais, consoantes = num_vogais_consoantes(frase)

print (f"frase possui {vogais} vogais")
print (f"e {consoantes} consoantes")