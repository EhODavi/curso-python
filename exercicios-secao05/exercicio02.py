numero = float(input('Informe um número: '))

if numero >= 0:
    print(f'A raiz quadrada de {numero} é {numero ** 0.5}!')
else:
    print(f'Não foi possível calcular a raiz quadrada (número negativo)!')
