while True:
    print('1 - Converter de km/h para m/s')
    print('2 - Converter de m/s para km/s')
    print('3 - Finalizar')
    opcao = int(input('\nInforme a opção: '))

    if opcao == 3:
        break

    velocidade = float(input('\nInforme a velocidade: '))

    if opcao == 1:
        print(f'\n{velocidade} km/h são {velocidade / 3.60} m/s\n')
    elif opcao == 2:
        print(f'\n{velocidade} m/s são {velocidade * 3.60} km/h\n')
