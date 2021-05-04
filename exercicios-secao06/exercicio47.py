while True:
    print('1 - Adição')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Saída\n')
    opcao = int(input('Informe a opção desejada: '))

    if opcao == 5:
        break

    numero1 = int(input('\nInforme o primeiro número: '))
    numero2 = int(input('Informe o segundo número: '))

    if opcao == 1:
        print(f'\n{numero1} + {numero2} = {numero1 + numero2}\n')
    elif opcao == 2:
        print(f'\n{numero1} - {numero2} = {numero1 - numero2}\n')
    elif opcao == 3:
        print(f'\n{numero1} * {numero2} = {numero1 * numero2}\n')
    elif opcao == 4:
        print(f'\n{numero1} / {numero2} = {numero1 / numero2}\n')
