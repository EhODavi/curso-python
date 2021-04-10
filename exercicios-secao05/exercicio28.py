print('1 - Média Geométrica;')
print('2 - Média Ponderada;')
print('3 - Média Harmônica;')
print('4 - Média Aritmética;')
opcao = int(input('Informe a opção: '))

x = int(input('Informe o primeiro número: '))
y = int(input('Informe o segundo número: '))
z = int(input('Informe o terceiro número: '))

if x > 0 and y > 0 and z > 0:
    if opcao == 1:
        print(f'Média Geométrica: {(x * y * z) ** (1/3)}')
    elif opcao == 2:
        print(f'Média Ponderada: {(x + 2 * y + 3 * z) / 6}')
    elif opcao == 3:
        print(f'Média Harmônica: {1 / ((1/x) + (1/y) + (1/z))}')
    elif opcao == 4:
        print(f'Média Aritmética: {(x + y + z) / 3}')
