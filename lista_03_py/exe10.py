#Crie uma função que receba um dicionário onde as chaves são nomes de alunos e
#os valores são listas de notas (com pesos na última posição). A função deve calcular
#a média ponderada de cada aluno usando reduce e retornar um novo dicionário
#com os resultados.
 
from functools import reduce

def notas(lista10):
    medias_finais = {}

    for aluno, valores in lista10.items():
        notas = valores[:-1]  #ultimo valor dentro da lista
        peso = valores[-1]  

        # Calcula a soma das notas 
        soma_ponderada = reduce(lambda acc, nota: acc + nota * peso, notas, 0)

        # Calcula a média ponderada
        media_final = soma_ponderada / (len(notas) * peso)

      
        medias_finais[aluno] = media_final  

    return medias_finais  

#entrada de teste
lista10 = {
    "João": [3, 7, 8, 9, 2],  # peso 2
    "Maria": [3, 5, 7, 5, 3]  # peso 3
}

resultados = notas(lista10)
print(resultados) 
