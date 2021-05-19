A = []
B = []

print('Preenchendo o vetor x:\n')

for i in range(10):
    numero = int(input('Informe um número: '))
    A.append(numero)

print('\nPreenchendo o vetor y:\n')

for i in range(10):
    numero = int(input('Informe um número: '))
    B.append(numero)

C = []

for i in range(10):
    if C.count(A[i]) == 0:
        C.append(A[i])
    if C.count(B[i]) == 0:
        C.append(B[i])

print(f'\nx = {A}')
print(f'y = {B}')
print(f'C = {C}')
