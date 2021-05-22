matriz = []
soma_coluna_impar = 0
soma = 0
soma1 = 0

for i in range(3):
    matriz.append([])

    for j in range(6):
        numero = float(input('Informe um número: '))
        matriz[i].append(numero)

        if (j + 1) % 2 != 0:
            soma_coluna_impar = soma_coluna_impar + numero

        if j == 1 or j == 3:
            soma = soma + numero

        if j == 0 or j == 1:
            soma1 = soma1 + numero

print('\nMatriz:\n')

for i in range(3):
    for j in range(6):
        print(f'{matriz[i][j]} ', end="")
    print()

for i in range(3):
    matriz[i][5] = soma1

print(f'\nSoma de todos os elementos das colunas ímpares: {soma_coluna_impar}')
print(f'Média aritmética dos elementos da segunda e quarta colunas: {soma / 6}')
print('Matriz modificada:\n')

for i in range(3):
    for j in range(6):
        print(f'{matriz[i][j]} ', end="")
    print()
