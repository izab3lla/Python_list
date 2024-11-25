#################### Peça três notas de um aluno e calcule a média aritmética delas ####################
#06#

def media(a, b, c):
        return  (a + b + c)/3

def valores():
        i = 1
        while i < 4:
           notas = float(input(f"Insira a nota {i}:"))
           i += 1
        return notas

print ("##### Calculadora de media de notas ##### \n")

notas = valores() 
media_final = media(notas)

print(media_final)

