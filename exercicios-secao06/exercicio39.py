base = float(input('Informe a base do triângulo: '))
altura = float(input('Informe a altura do triângulo: '))

if base > 0 and altura > 0:
    print(f'Área do triângulo: {(base * altura) / 2}')
else:
    print('Valores inválidos!')
