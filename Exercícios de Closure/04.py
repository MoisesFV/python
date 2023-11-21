# Closures em uma lista: Escreva uma função criar_closures(n) 
# que retorna uma lista de n closures, onde o i-ésimo closure retorna o valor de i.

def criar_closures(n):
    closures = []
    for i in range(n):
        closures.append(lambda x=i: x)
    return closures

closures = criar_closures(5)
for i in range(5):
    print(closures[i]()) 

#a IA do Bing teve dificuldade com essa resposta
#trazendo print(closuresi) ao invés de print(closures[i]()) (20/11/2023)