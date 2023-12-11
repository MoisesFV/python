# Closure com múltiplos estados: Escreva 
# uma função criar_calculadora() que retorna 
# um closure que pode realizar adição, subtração, multiplicação e divisão. 
# O closure deve lembrar o resultado da última operação e usá-lo 
# como o primeiro operando para a próxima operação.

def criar_calculadora():
    resultado = [0]
    def op(x,operacao):
        if operacao == 'adicao':
            resultado[0] += x
        elif operacao == 'subtracao':
            resultado[0] -= x
        elif operacao == 'multiplicacao':
            resultado[0] *= x
        elif operacao == 'divisao':
            resultado[0] /= x
        return resultado[0]
    return op


cria_calculadora = criar_calculadora()
print(cria_calculadora(5,'adicao'))
print(cria_calculadora(2,'subtracao'))
print(cria_calculadora(2,'multiplicacao'))
print(cria_calculadora (2,'divisao'))