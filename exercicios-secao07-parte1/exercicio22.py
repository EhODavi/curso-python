A = []
B = []

print('Preenchendo o vetor A:\n')

for i in range(10):
    numero = int(input('Informe um número: '))
    A.append(numero)

print('\nPreenchendo o vetor B:\n')

for i in range(10):
    numero = int(input('Informe um número: '))
    B.append(numero)

C = []

for i in range(10):
    if i % 2 == 0:
        C.append(A[i])
    else:
        C.append(B[i])

print(f'\nC: {C}')
