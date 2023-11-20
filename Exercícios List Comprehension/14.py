# Exercício 4: Dada a lista de dicionários abaixo, use uma compreensão 
# de lista para criar uma nova lista com os dicionários que têm 
# um valor de ‘preco’ maior que 50, ordenados pelo valor da chave 
# ‘preco’ em ordem decrescente. (Exercício criado por IA)

produtos = [
    {'nome': 'Produto 5', 'preco': 55.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 75.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

new_produtos = [produto for produto in produtos
                if produto['preco'] > 50]
new_produtos = sorted(new_produtos, key=lambda p : p['preco'], reverse=True)

print(new_produtos)