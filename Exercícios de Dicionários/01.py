# Ordenar por chave: Dado o dicionário {'b': 1, 'a': 2, 'c': 3}, 
# escreva um código para ordená-lo por chave. (Exercício criado por IA)

dicionario = {'b': 1, 'a': 2, 'c': 3}

new_dicionario = dict(sorted(dicionario.items()))

print(new_dicionario)