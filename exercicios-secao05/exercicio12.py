import math

numero = int(input('Informe um número inteiro: '))

if numero > 0:
    print(f'O logaritmo do número {numero} é {math.log(numero)}')
else:
    print('NÚMERO INVÁLIDO!')
