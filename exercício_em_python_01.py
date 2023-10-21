"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

#Variável letra que será inserida
letra = ''

#Palavra a ser adivinhada
palavra = 'abracadabra'

#Letras já acertadas
acertos = ''

#Tentativas, excluídas as letras repetidas e caracteres inválidos
tentativas = 0

tamanho = len(palavra)

#Todos os caracteres já usados
letras_usadas = ''

while True:
    letra = input('Digite uma letra: ')
    #Caso não seja caractere do alfabeto
    if not letra.isalpha():
        print('Letra inválida')
        continue
    #Caso inclua mais de um caractere
    if len(letra) > 1:
        print('Somente uma letra é permitida!')
        continue
    #Caso já tenha acertado a letra
    if letra in acertos:
        print('Letra já digitada!')
        continue
    #Caso seja uma letra já usada
    if letra in letras_usadas:
        print('Letra já digitada!')
        continue
    #Avisa que a letra não foi encontrada
    if letra not in palavra:
        letras_usadas = letras_usadas + letra
        print('Não tem essa letra na palavra!')
        tentativas += 1
        continue
    tentativas += 1
    letras_usadas = letras_usadas + letra

    #Checa as letras da palavra
    for letras in palavra:
        #Se a letra digitada está na palavra, adiciona aos acertos
        if letras == letra:
            acertos = acertos + letras    
    print('Palavra formada até agora:')
    #Imprimirá os caracteres já descobertos ou asteriscos, checa cada caractere da palavra
    for descobrir in palavra:
        #Se o caractere já foi descoberto, imprime
        if descobrir in acertos:
            print(descobrir, end = ' ')
        #Senão imprime um asterisco
        else:
            print('*', end = ' ')        
    print('')
    #Caso tenha acertado todas as letras, dá um break e termina o laço, encerrando o jogo
    if len(acertos) == tamanho:
        break
    else:
        continue
os.system('cls')
print(f'Jogo encerrado, a palavra era: {palavra.upper()}, total de tentativas = {tentativas}')




    

