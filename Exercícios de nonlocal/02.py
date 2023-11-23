# Acumulador de Soma: Escreva uma função chamada 
# acumulador_soma que retorna uma função interna. 
# A função interna deve aceitar um número, adicionar 
# esse número a um total acumulado e retornar o total 
# acumulado. Use nonlocal para fazer isso.

def acumulador_soma():
    num = 0
    def soma(x):
        nonlocal num
        num += x
        return num
    return soma

somar = acumulador_soma()

print(somar(3))
print(somar(1))
print(somar(4))
print(somar(3))
print(somar(2))
print(somar(7))
print(somar(1))