# Transforme esse dicionário em uma lista de tuplas no formato 
# (nome_do_estudante, disciplina, nota). 
# Por exemplo, uma entrada da lista seria ('Ana', 'Matemática', 90).

# Em seguida, use a função groupby para agrupar os estudantes pelas disciplinas. 
# Para isso, você precisará:

# Ordenar a lista de estudantes pelo nome.
# Usar groupby para agrupar as notas por estudante.
# Exibir o nome de cada estudante e suas notas em cada disciplina.
from itertools import groupby

estudantes_notas = {
    'Ana': {'Matemática': 90, 'Ciências': 85, 'Português': 92},
    'Bruno': {'Matemática': 88, 'Ciências': 79, 'Português': 95},
    'Carla': {'Matemática': 91, 'Ciências': 88, 'Português': 85},
    'Diego': {'Matemática': 76, 'Ciências': 73, 'Português': 80},
    'Eva': {'Matemática': 92, 'Ciências': 89, 'Português': 94}
}






new_lista = []

for nome, materias in estudantes_notas.items():
    for materia, nota in materias.items():
       new_lista.append((nome,materia,nota))

new_lista = groupby(new_lista, key=lambda a : a[0])

for nome, dados in new_lista:
    print(nome)
    for dado in dados:
        print(dado)
 










