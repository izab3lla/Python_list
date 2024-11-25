####################Peça ao usuário dois números e uma operação (adição, subtração, multiplicação ou divisão) e execute a operação escolhida.####################
#24#

def anagrama(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    if sorted(s1)== sorted(s2):
     return True

print ("##### Bem vindo ao indentificador de anagramas!! ##### \n")

s1 = input("Digite a primeira palavra:")
s2 = input("Digite a segunda palavra:")

if anagrama(s1, s2):
   print("sao anagramas!")
else: 
   print("Nao sao anagramas!")