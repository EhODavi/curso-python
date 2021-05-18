vetor = []

for i in range(10):
    numero = int(input('Informe um número: '))

    if numero < 0:
        vetor.append(0)
    else:
        vetor.append(numero)

print(f'Vetor: {vetor}')
