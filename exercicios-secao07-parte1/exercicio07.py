numeros = []

for i in range(10):
    numero = int(input('Informe um número: '))
    numeros.append(numero)

maior_elemento = numeros[0]
posicao_maior_elemento = 0

for i in range(1, 10):
    if numeros[i] > maior_elemento:
        maior_elemento = numeros[i]
        posicao_maior_elemento = i

print(f'Vetor: {numeros}')
print(f'Maior elemento: {maior_elemento}')
print(f'Posição do maior elemento: {posicao_maior_elemento}')
