vetor = []
quantidade = 0

while quantidade < 10:
    numero = int(input('Informe um número: '))

    if vetor.count(numero) == 0:
        vetor.append(numero)
        quantidade = quantidade + 1

print(f'\nVetor = {vetor}')
