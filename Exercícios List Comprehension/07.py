# 7-Dada uma lista de nomes, crie uma nova lista apenas com os nomes que começam com a letra "A".

list = ['Mico', 'Xexéu', 'Alce', 'Camelo', 'Zebra', 'Vitória-régia',
        'Framboesa', 'Panda', 'Quiuí', 'Banana', 'Hipopótamo', 'Nectarina',
        'Vaca', 'Limão', 'Leão', 'Tigre', 'Abacate', 'Uva', 'Kiwi', 'Borboleta',
        'Xixá', 'Dinossauro', 'Zimbro', 'Elefante', 'Blueberry', 'Pêssego',
        'Maçã', 'Goiaba', 'Sapoti', 'Iguana', 'Urso', 'Cachorro', 'Aranha',
        'Caqui', 'Abacaxi', 'Koala', 'Tangerina', 'Damasco', 'Anta',
        'Baleia', 'Ameixa', 'Quokka', 'Oxicoco', 'Falcão', 'Jabuticaba',
        'Avestruz', 'Amora', 'Inhame', 'Cereja', 'Naja', 'Rinoceronte',
        'Serpente', 'Gato', 'Rambutão', 'Escarlate', 'Ornitorrinco',
        'Hortelã', 'Jaguar']

new_list = [word for word in list
            if word.startswith('A')]

print(new_list)