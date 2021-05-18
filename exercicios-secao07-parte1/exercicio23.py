A = []
B = []

print('Preenchendo o vetor A:\n')

for i in range(5):
    numero = float(input('Informe um número: '))
    A.append(numero)

print('\nPreenchendo o vetor B:\n')

for i in range(5):
    numero = float(input('Informe um número: '))
    B.append(numero)

produto_escalar = 0

for i in range(5):
    produto_escalar = produto_escalar + (A[i] * B[i])

print(f'\nA: {A}')
print(f'B: {B}')
print(f'Produto Escalar: {produto_escalar}')
