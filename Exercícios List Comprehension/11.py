# Exercício 1: Dada a lista de dicionários abaixo, use 
# uma compreensão de lista para criar uma nova lista 
# com os dicionários ordenados pelo valor da chave ‘nome’ 
# em ordem alfabética. (Exercício criado por IA)

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

new_list = [
    chave for chave in produtos
]
new_list = sorted(new_list, key=lambda n : n['nome'])
print(new_list)