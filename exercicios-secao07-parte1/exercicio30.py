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
    if B.count(A[i]) > 0 and C.count(A[i]) == 0:
        C.append(A[i])

print(f'\nx = {A}')
print(f'y = {B}')
print(f'C = {C}')
