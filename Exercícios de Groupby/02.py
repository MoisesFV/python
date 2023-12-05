# Exercício 2: Agrupamento de strings Dada a seguinte lista de 
# strings, agrupe as strings por seu primeiro caractere:

# Python
# Código gerado por IA. Examine e use com cuidado. 
# Mais informações em perguntas frequentes.

from itertools import groupby
# Lista de palavras
words = ['orange', 'banana', 'cherry', 'elderberry', 'date' , 'fig', 'grape','apple', 'coco']

words.sort(key=lambda inicial : inicial[0])

ordenado = groupby(words, key=lambda a : a[0])

for key, word in ordenado:
    print(key, list(word))