####################Peça uma lista de notas de alunos e calcule a média. Em seguida, retorne uma lista com as notas que são maiores do que a média ####################
#13#
print ("##### Vamos descobrir a maior nota ##### \n")

def media_notas(notas):
    media = sum(notas) / len(notas)
    maior_nota = [nota for nota in notas if nota > media]
    return media, maior_nota

valores = int(input("Digite a quantidade de notas que deseja receber a media \n"))

notas = []
for x in range(valores):
    nota = float(input("Digite a nota:"))
    notas.append(nota)

media, maior_nota = media_notas(notas)

print (f"A media final eh:{media} \n")
print (f"Os numero acima da media sao: {maior_nota}")