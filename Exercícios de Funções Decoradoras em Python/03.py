# Decorador de verificação de tipo: 
# Crie um decorador que verifique se os 
# argumentos passados para uma função decorada são do tipo correto.

def check(func):
    def wrapper(a, b):
        if type(a) != int  or type(b) != int:
            raise TypeError('Tipo de dado deve ser "int"')
        return func(a,b)
        
    return wrapper

@check
def soma(a,b):
    return a+b

print(soma(5, 2))

