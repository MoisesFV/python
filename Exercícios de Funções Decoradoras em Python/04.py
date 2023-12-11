# Decorador de contagem de chamadas: 
# Crie um decorador que mantenha um 
# registro de quantas vezes uma função 
# decorada foi chamada.

cont = {}
def contador(func):
    cont[func.__name__] = [0]
    def wrapper(*a):
        cont[func.__name__][0] += 1
        print(f'função {func.__name__}, chamada {cont[func.__name__]} vez(es)')
        return func(*a)
    return wrapper

@contador    
def soma(a,b):
    return a+b

print(soma(5,2))
print(soma(5,2))
print(soma(5,2))
print(soma(5,2))

@contador 
def teste():
    print('teste')

teste()
print(soma(5,2))