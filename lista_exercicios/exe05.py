####################  Receba um número inteiro e exiba a tabuada dele (multiplicações de 1 a 10) ####################
#05#

def tabu (num):
    i = 0
    while i <= 10:
       tabu =  num * i 
       print (f"{num} X {i} = {tabu}")
       i += 1 

print ("##### Escolha o numero que deseja ver a tabuada: ##### \n")

n = int(input("Digite um numero: \n"))
tabuada = tabu(n) 

print(tabuada)

#ver o none aparece
#esta aparecendo numero maiores que 10