decimo_digito = 0
decimo_primeiro_digito = 0
ini1 = 10
ini2 = 11
print('Digite 11 dígitos do CPF, sem espaços, pontos ou traços: ')
#lista com números do cpf para usar append
cpf = []
cpf_entrada = input()
#testa se são números
if not cpf_entrada.isdigit():
    print('Algum digito foi inserido errado')
#testa o tamanho do cpf(11 dígitos)
if cpf_entrada.isdigit() and len(cpf_entrada) < 11 or len(cpf_entrada) > 11:
    print(f'São 11 dígitos, você digitou {len(cpf_entrada)} dígitos')
else:
    #insere os números na lista
    for i in range(11):
        cpf.append(cpf_entrada[i])
    #calcula o décimo dígito       
    for i in range(9):
        decimo_digito+=int(cpf[i])*ini1
        ini1 -= 1
    decimo_digito = decimo_digito % 11
    cpf[9] = str(0) if decimo_digito < 2 else str(11 - decimo_digito)
    #calcula o décimo primeiro dígito
    for i in range(10):
        decimo_primeiro_digito+=int(cpf[i])*ini2
        ini2 -= 1
    decimo_primeiro_digito = decimo_primeiro_digito % 11
    cpf[10] = str(0) if decimo_primeiro_digito < 2 else str(11 - decimo_primeiro_digito)
    #une a lista
    cpf_saida = ''.join(cpf)
    #separa o cpf em duas partes para formatá-lo na saída
    cpfpart1 = cpf_saida[0:9]
    cpfpart2 = cpf_saida[9:11]
    #Checa se o cpf formatado é válido e exibe a informação, junto com o CPF formatado
    print(f'CPF {cpfpart1+'-'+cpfpart2} VÁLIDO') if cpf == list(cpf_entrada) else print(f'CPF {cpfpart1+'-'+cpfpart2} INVÁLIDO')