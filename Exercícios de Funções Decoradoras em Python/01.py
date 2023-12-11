# Decorador de registro: 
# Crie um decorador que registre a 
# execução de qualquer função decorada. 
# Ele deve imprimir uma mensagem antes e 
# depois da execução da função.

def register_exec(func):
    def wrapper(*args,**kwargs):
        print('Começou a execução...')
        result = func(*args, **kwargs)
        print(result)
        print('Finalizou a execução')
        return result
    return wrapper    




@register_exec
def soma(a,b):
    return(a+b)   

soma(6,3)