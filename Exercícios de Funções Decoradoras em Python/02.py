# Decorador de temporização: 
# Crie um decorador que registre o 
# tempo que leva para executar a função decorada.

import time

def timer(func):
    def wrapper(*args,**kwargs):
        ini = time.perf_counter()
        result = func(*args,**kwargs)
        final = time.perf_counter()
        print('Tempo gasto na execução: ', final-ini)
        return result
    return wrapper

@timer
def contador(a):
    for i in range(a):
        print(i)

contador(10)


