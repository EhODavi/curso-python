vetor = []

for i in range(10):
    numero = int(input('Informe um número: '))
    vetor.append(numero)

x = int(input('Informe um número x: '))

vetor_multiplo_x = []

for i in range(10):
    if vetor[i] % x == 0 and vetor_multiplo_x.count(vetor[i]) == 0:
        vetor_multiplo_x.append(vetor[i])

print(f'Vetor: {vetor}')
print(f'Vetor dos múltiplos de {x}: {vetor_multiplo_x}')
