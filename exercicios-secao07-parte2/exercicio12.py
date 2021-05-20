matriz = []

for i in range(3):
    matriz.append([])

    for j in range(3):
        numero = int(input('Informe um número: '))

        matriz[i].append(numero)

matriz_transposta = []

for i in range(3):
    matriz_transposta.append([])

    for j in range(3):
        matriz_transposta[i].append(matriz[j][i])

print(f'\nMatriz:\n')

for i in range(3):
    for j in range(3):
        print(f'{matriz[i][j]} ', end="")

    print()

print(f'\nMatriz transposta:\n')

for i in range(3):
    for j in range(3):
        print(f'{matriz_transposta[i][j]} ', end="")

    print()
