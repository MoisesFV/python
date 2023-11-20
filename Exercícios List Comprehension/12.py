# Exercício 2: Dada a lista de dicionários abaixo, use uma 
# compreensão de lista para criar uma nova lista com os 
# dicionários ordenados pelo valor da chave ‘idade’ 
# em ordem decrescente. (Exercício criado por IA)

pessoas = [
    {'nome': 'João', 'idade': 25},
    {'nome': 'Maria', 'idade': 30},
    {'nome': 'Pedro', 'idade': 20},
    {'nome': 'Ana', 'idade': 35},
    {'nome': 'Carlos', 'idade': 28},
]

pessoas_idade = [
    lista for lista in pessoas
]
pessoas_idade = sorted(pessoas_idade, key=lambda i : i['idade'], reverse=True)

print(pessoas_idade)
