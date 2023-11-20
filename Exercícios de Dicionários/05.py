# Ordenar por chave em ordem decrescente: Dado o dicionário {'b': 1, 'a': 2, 'c': 3}, 
# escreva um código para ordená-lo por chave em ordem decrescente.

dicionario = {'b': 1, 'a': 2, 'c': 3}

new_dicionario = dict(sorted(dicionario.items(), key=lambda chave : chave[1], reverse=True))

print(new_dicionario)