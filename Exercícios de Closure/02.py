# Closure com estado: Escreva uma função contador() 
# que retorna um closure que não recebe argumentos e 
# retorna um novo número inteiro a cada vez que é chamado, 
# começando com 1 e incrementando a cada chamada.

def contador():
    i = [0]
    def contagem():
        i[0]+= 1
        return i[0]
    return contagem

progressao =  contador()

print(progressao())
print(progressao())
print(progressao())
print(progressao())