A = []

print('Lendo a matriz A:')

for i in range(3):
    A.append([])

    for j in range(3):
        numero = float(input())
        A[i].append(numero)

B = []

for i in range(3):
    B.append([])

    for j in range(3):
        soma = 0

        for k in range(3):
            soma = soma + (A[i][k] * A[k][j])

        B[i].append(soma)

print('\nMatriz B:')

for i in range(3):
    for j in range(3):
        print(f'{B[i][j]} ', end="")
    print()
