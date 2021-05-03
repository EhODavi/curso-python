valor_inicial = int(input('Digite o valor inicial: '))
valor_final = int(input('Digite o valor final: '))

if valor_inicial <= valor_final:
    soma = 0

    for i in range(valor_inicial, valor_final + 1):
        if i % 2 != 0:
            soma = soma + i

    print(f'Soma dos ímpares neste intervalo: {soma}')
else:
    print('Intervalo de valores inválido')
