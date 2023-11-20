# Exercício 5: Dada a lista de dicionários abaixo, use uma 
# compreensão de lista para criar uma nova lista
# com os dicionários que têm um valor de ‘idade’ menor que 30, 
# ordenados pelo valor da chave ‘idade’ em ordem crescente.
# (Exercício criado por IA)

pessoas = [
    {'nome': 'João', 'idade': 25},
    {'nome': 'Maria', 'idade': 30},
    {'nome': 'Pedro', 'idade': 20},
    {'nome': 'Ana', 'idade': 35},
    {'nome': 'Carlos', 'idade': 28},
]

new_pessoas = [
    pessoa for pessoa in pessoas
    if pessoa['idade'] < 30
]
new_pessoas = sorted(new_pessoas, key=lambda i : i['idade'])

print(new_pessoas)