vetor = []
vetor_compactado = []

for i in range(15):
    numero = int(input('Informe um número: '))
    vetor.append(numero)

    if numero != 0:
        vetor_compactado.append(numero)

print(f'\nVetor = {vetor}')
print(f'Vetor compactado = {vetor_compactado}')
