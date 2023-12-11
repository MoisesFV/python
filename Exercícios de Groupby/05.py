# Exercício 1: Dada a lista de tuplas 
# estudantes = [('john', 'A', 15), 
#               ('jane', 'B', 12), ('dave', 'B', 10)], 
# use a função groupby do módulo itertools para 
# agrupar os estudantes pela segunda entrada 
# da tupla (ou seja, ‘A’ ou ‘B’).

from itertools import groupby

estudantes = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]

new_estudantes = sorted(estudantes, key=lambda x : x[1])

for chave, estudantes in groupby(new_estudantes, key=lambda x : x[1]):
    print(chave, list(estudantes))

