# Ordenar por comprimento da chave: Dado o dicionário {'banana': 1, 'maçã': 2, 'uva': 3}, 
# escreva um código para ordená-lo pelo comprimento da chave.

dicionario = {'banana': 1, 'maçã': 2, 'uva': 3}

new_dicionario = dict(sorted(dicionario.items(), key=lambda item : len(item[0])))

print(new_dicionario)