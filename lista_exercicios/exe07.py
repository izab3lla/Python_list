#################### Receba uma palavra e exiba-a invertida (exemplo: "Python->"nohtyP"). ####################
#07#

def inv(palavra):
    return palavra[::-1]

print ("##### Bem vindo ao inversor de palavras! ##### \n")
letra = str(input("Digite a palavra que deseja inverter:"))
inverso = inv(letra)

print(f"A palavra {letra} invertida fica: {inverso}")