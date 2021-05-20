matriz = []

for i in range(4):
    matriz.append([])

    for j in range(4):
        numero = int(input('Informe um número: '))

        matriz[i].append(numero)

maior_valor = (matriz[0][0], 0, 0)

print(f'\nMatriz:\n')

for i in range(4):
    for j in range(4):
        print(f'{matriz[i][j]} ', end="")

        if matriz[i][j] > maior_valor[0]:
            maior_valor = (matriz[i][j], i, j)

    print()

print(f'\nO maior valor ({maior_valor[0]}) está na linha {maior_valor[1]} e coluna {maior_valor[2]}!')
