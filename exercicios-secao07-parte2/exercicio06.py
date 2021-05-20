matrizA = []

print('Lendo a matriz A:\n')

for i in range(4):
    matrizA.append([])

    for j in range(4):
        numero = int(input('Informe um número: '))

        matrizA[i].append(numero)

matrizB = []

print('\nLendo a matriz B:\n')

for i in range(4):
    matrizB.append([])

    for j in range(4):
        numero = int(input('Informe um número: '))

        matrizB[i].append(numero)

matrizC = []

for i in range(4):
    matrizC.append([])

    for j in range(4):
        if matrizA[i][j] >= matrizB[i][j]:
            matrizC[i].append(matrizA[i][j])
        else:
            matrizC[i].append(matrizB[i][j])


print(f'\nMatriz A:')

for i in range(4):
    for j in range(4):
        print(f'{matrizA[i][j]} ', end="")

    print()

print(f'\nMatriz B:')

for i in range(4):
    for j in range(4):
        print(f'{matrizB[i][j]} ', end="")

    print()

print(f'\nMatriz C:')

for i in range(4):
    for j in range(4):
        print(f'{matrizC[i][j]} ', end="")

    print()
