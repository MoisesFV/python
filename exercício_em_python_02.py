lista = []
while True:
    print('Selecione uma opção: ')
    opcao = input('[I]nserir, [R]emover último item, [L]istar itens, [S]air: ').lower()
    if opcao.isalpha:
        if opcao.startswith('i'):
            inserir = input('O que deseja inserir na lista? ')
            lista.append(inserir)
            print(f'{inserir}, adicionado a lista')
        elif opcao.startswith('l'):
            print('Lista: ')
            for itens in lista:
                print(itens)
        elif opcao.startswith('r'):
            lista.pop()
            print('Último item removido')
        elif opcao.startswith('s'):
            print('Programa encerrado')
            break
        else:
            print('Comando desconhecido')