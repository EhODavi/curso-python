vetor = []
vetor_repetidos = []

for i in range(10):
    numero = int(input('Informe um número: '))
    vetor.append(numero)

    if vetor.count(numero) == 2:
        vetor_repetidos.append(numero)

print(f'Vetor: {vetor}')
print(f'Vetor repetidos: {vetor_repetidos}')
