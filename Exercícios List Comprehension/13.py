# Exercício 3: Dada a lista de dicionários abaixo, 
# use uma compreensão de lista para criar uma 
# nova lista com os dicionários ordenados 
# pelo comprimento do valor da chave ‘nome’ em 
# ordem crescente. (Exercício criado por IA)

palavras = [
    {'nome': 'casa', 'frequencia': 10},
    {'nome': 'automóvel', 'frequencia': 5},
    {'nome': 'Python', 'frequencia': 20},
    {'nome': 'computador', 'frequencia': 7},
    {'nome': 'caneta', 'frequencia': 15},
]

new_palavras = [
    palavra for palavra in palavras
]
new_palavras = sorted(new_palavras, key=lambda n : n['nome'])


print(new_palavras)