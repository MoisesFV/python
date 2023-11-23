# Contador Incremental: Escreva uma função chamada criar_contador 
# que retorna uma função interna. A função interna deve incrementar 
# um contador cada vez que é chamada e retornar o valor atual do 
# contador. Use nonlocal para fazer isso.

def criar_contador():
    cont = 0
    def contar():
        nonlocal cont
        cont+= 1
        return cont
    return contar

contador = criar_contador()
print(contador())
print(contador())
print(contador())
print(contador())