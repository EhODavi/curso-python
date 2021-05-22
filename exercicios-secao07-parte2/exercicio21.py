matrizA = []

print('Lendo a matriz A:')

for i in range(2):
    matrizA.append([])

    for j in range(2):
        numero = float(input())
        matrizA[i].append(numero)

matrizB = []

print('\nLendo a matriz B:')

for i in range(2):
    matrizB.append([])

    for j in range(2):
        numero = float(input())
        matrizB[i].append(numero)

print('\n(a) somar as duas matrizes')
print('(b) subtrair a primeira matriz da segunda')
print('(c) adicionar uma constante às duas matrizes')
print('(d) imprimir as matrizes')
opcao = input('\nInforme uma opção: ')

if opcao == 'a':
    print('\nMatriz A:')

    for i in range(2):
        for j in range(2):
            print(f'{matrizA[i][j]} ', end="")
        print()

    print('\nMatriz B:')

    for i in range(2):
        for j in range(2):
            print(f'{matrizB[i][j]} ', end="")
        print()

    matrizC = []

    for i in range(2):
        matrizC.append([])

        for j in range(2):
            matrizC[i].append(matrizA[i][j] + matrizB[i][j])

    print('\nMatriz C:')

    for i in range(2):
        for j in range(2):
            print(f'{matrizC[i][j]} ', end="")
        print()
elif opcao == 'b':
    print('\nMatriz A:')

    for i in range(2):
        for j in range(2):
            print(f'{matrizA[i][j]} ', end="")
        print()

    print('\nMatriz B:')

    for i in range(2):
        for j in range(2):
            print(f'{matrizB[i][j]} ', end="")
        print()

    matrizC = []

    for i in range(2):
        matrizC.append([])

        for j in range(2):
            matrizC[i].append(matrizA[i][j] - matrizB[i][j])

    print('\nMatriz C:')

    for i in range(2):
        for j in range(2):
            print(f'{matrizC[i][j]} ', end="")
        print()
elif opcao == 'c':
    constante = float(input('\nInforme o valor da constante: '))

    print('\nMatriz A antes:')

    for i in range(2):
        for j in range(2):
            print(f'{matrizA[i][j]} ', end="")
        print()

    print('\nMatriz B antes:')

    for i in range(2):
        for j in range(2):
            print(f'{matrizB[i][j]} ', end="")
        print()

    for i in range(2):
        for j in range(2):
            matrizA[i][j] = matrizA[i][j] + constante
            matrizB[i][j] = matrizB[i][j] + constante

    print('\nMatriz A depois:')

    for i in range(2):
        for j in range(2):
            print(f'{matrizA[i][j]} ', end="")
        print()

    print('\nMatriz B depois:')

    for i in range(2):
        for j in range(2):
            print(f'{matrizB[i][j]} ', end="")
        print()
else:
    print('\nMatriz A:')

    for i in range(2):
        for j in range(2):
            print(f'{matrizA[i][j]} ', end="")
        print()

    print('\nMatriz B:')

    for i in range(2):
        for j in range(2):
            print(f'{matrizB[i][j]} ', end="")
        print()
