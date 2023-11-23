# Gerador de Sequência: Escreva uma função chamada 
# gerador_sequencia que aceita um número inicial n 
# e retorna uma função interna. A função interna 
# deve retornar o próximo número na sequência cada 
# vez que é chamada, começando com n. Use nonlocal 
# para fazer isso.

def gerador_sequencia(n):
    num = n
    def proximo():
        nonlocal num
        num+= 1
        return num
    return proximo

sequencia = gerador_sequencia(3)

print(sequencia())
print(sequencia())
print(sequencia())
print(sequencia())



    