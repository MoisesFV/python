# Closure simples: Escreva uma função criar_multiplicador(x) 
# que retorna um closure que multiplica seu argumento por x. 
# Por exemplo, multiplica_por_dois = criar_multiplicador(2) 
# deve retornar uma função que multiplica seu argumento por 2.

def criar_multiplicador(x):
    def retarda(y):
        return x*y
    return retarda


multiplica_por_dois = criar_multiplicador(2)

print(multiplica_por_dois(8))







