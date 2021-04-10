altura = float(input('Informe a altura da pessoa: '))
sexo = input('Informe o sexo da pessoa (M ou F): ')

if sexo == 'M':
    print(f'Peso ideal: {(72.7 * altura) - 58}')
elif sexo == 'F':
    print(f'Peso ideal: {(62.1 * altura) - 44.7}')
