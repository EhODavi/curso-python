A = []

print('Lendo a matriz A:')

for i in range(3):
    A.append([])

    for j in range(3):
        numero = float(input())
        A[i].append(numero)

B = []

print('\nLendo a matriz B:')

for i in range(3):
    B.append([])

    for j in range(3):
        numero = float(input())
        B[i].append(numero)

C = []

for i in range(3):
    C.append([])

    for j in range(3):
        soma = 0

        for k in range(3):
            soma = soma + (A[i][k] * B[k][j])

        C[i].append(soma)

print('\nMatriz C:')

for i in range(3):
    for j in range(3):
        print(f'{C[i][j]} ', end="")
    print()
