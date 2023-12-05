# Exercício 1: Agrupamento simples Dada a seguinte 
# lista de números, agrupe os números por paridade 
# (par ou ímpar):(Exercício proposto por IA)

from itertools import groupby

# Lista de números
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10]

paridade = groupby(numbers, key=lambda a:a % 2 ==0)

for key, number in paridade:
    if key == True:
        print('Par:', list(number))
    else:
        print('ímpar:',list(number))

