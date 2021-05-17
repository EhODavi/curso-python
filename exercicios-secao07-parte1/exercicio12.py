vetor = []

for i in range(5):
    numero = float(input('Informe um número: '))
    vetor.append(numero)

maior = vetor[0]
menor = vetor[0]

for i in range(1, 5):
    if vetor[i] > maior:
        maior = vetor[i]
    if vetor[i] < menor:
        menor = vetor[i]

print(f'Vetor: {vetor}')
print(f'Maior valor: {maior}')
print(f'Menor valor: {menor}')
print(f'Média: {sum(vetor) / 5}')
