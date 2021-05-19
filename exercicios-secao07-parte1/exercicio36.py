vetor = []

for i in range(10):
    numero = float(input('Informe um número: '))
    vetor.append(numero)

print(f'\nVetor antigo: {vetor}')
vetor.sort()
print(f'Vetor novo: {vetor}')
