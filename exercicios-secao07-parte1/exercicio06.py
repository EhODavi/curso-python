vetor = []

for i in range(10):
    numero = int(input('Informe um número: '))
    vetor.append(numero)

maior_numero = vetor[0]
menor_numero = vetor[0]

for i in range(1, 10):
    if vetor[i] > maior_numero:
        maior_numero = vetor[i]
    if vetor[i] < menor_numero:
        menor_numero = vetor[i]

print(f'Vetor: {vetor}')
print(f'Maior valor: {maior_numero}')
print(f'Menor valor: {menor_numero}')
