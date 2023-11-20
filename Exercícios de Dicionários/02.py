# Ordenar por valor: Dado o dicionário {'b': 1, 'a': 2, 'c': 3}, 
# escreva um código para ordená-lo por valor.

dicionario = {'b': 1, 'a': 2, 'c': 3}

new_dicionario = dict(sorted(dicionario.items(), key=lambda item : item[1]))

print(new_dicionario)