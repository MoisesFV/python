# 3-Dada uma lista de palavras, crie uma nova lista contendo o tamanho de cada palavra
list = ['Tartaruga', 'Vaca', 'Vachorro', 'Elefante', 'Tigre', 'Avestruz']
tam = [[f'Animal : {x}, tamanho em letras: {len(x)}' for x in list]]
print(tam)