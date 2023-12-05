# Exercício 4: 
# Agrupamento com ordenação 
# Dada a seguinte lista de números, 
# ordene a lista em ordem crescente e 
# depois agrupe os números por paridade 
# (par ou ímpar):

# Python
# Código gerado por IA. Examine e use com cuidado. 
# Mais informações em perguntas frequentes.

from itertools import groupby
numbers = [6, 1, 9, 4, 2, 8, 7, 5, 3]

numbers = sorted(numbers)

numbers = groupby(list(numbers), key=lambda a : a % 2 == 0)

for key, number in numbers:
    if key == True:
        print('Par', list(number))
    else:
        print('ímpar', list(number))