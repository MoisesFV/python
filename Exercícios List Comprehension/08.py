# 8-Dada uma lista de frutas, crie uma nova lista com o comprimento de cada fruta, apenas para as frutas com mais de 5 letras.

frutas = ["Maçã", "Banana", "Cereja", "Damasco", "Elderberry",
           "Figo", "Goiaba", "Honeydew", "Icaco", "Jaca", "Kiwi",
             "Limão", "Manga", "Nectarina", "Laranja", "Papaia",
            "Quince", "Rambutan", "Morango", "Tangerina"]

frutas_tam = [[fruta, f'Tamanho em letras: {len(fruta)}'] for fruta in frutas
              if len(fruta) > 5]

print(frutas_tam)