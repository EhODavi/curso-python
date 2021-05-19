A = []

for i in range(11):
    numero = float(input('Informe um número: '))
    A.append(numero)

print(f'\nVetor antigo: {A}')
A.sort()
print(f'Vetor novo: {A}')
