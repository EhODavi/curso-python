vetor = []

for i in range(5):
    numero = float(input('Informe um número: '))
    vetor.append(numero)

maior = vetor[0]
menor = vetor[0]
maior_posicao = 0
menor_posicao = 0

for i in range(1, 5):
    if vetor[i] > maior:
        maior = vetor[i]
        maior_posicao = i
    if vetor[i] < menor:
        menor = vetor[i]
        menor_posicao = i

print(f'Posição do maior: {maior_posicao}')
print(f'Posição do menor: {menor_posicao}')
