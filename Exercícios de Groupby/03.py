# Exercício 3: Agrupamento com função chave 
# personalizada Dada a seguinte lista de tuplas, 
# agrupe as tuplas por seu segundo elemento:

# Python
# Código gerado por IA. Examine e use com cuidado. 
# Mais informações em perguntas frequentes.

from itertools import groupby
tuples = [('a', 1), ('b', 1), ('c', 2), ('d', 2), ('e', 3), ('f', 3)]

tuples.sort(key=lambda a : a[1])

ordened_tuples = groupby(tuples, key=lambda a : a[1])

for key, tuple in ordened_tuples:
    print(key, list(tuple))