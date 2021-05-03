while True:
    numero = float(input('Informe um número: '))

    if numero <= 0:
        break

    print(f'O quadrado de {numero} é {numero ** 2}')
    print(f'O cubo de {numero} é {numero ** 3}')
    print(f'A raiz quadrada de {numero} é {numero ** (1/2)}')
