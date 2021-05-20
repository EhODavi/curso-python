matriz = []
soma = 0

for i in range(3):
    matriz.append([])

    for j in range(3):
        numero = int(input('Informe um número: '))

        matriz[i].append(numero)

        if j > i:
            soma = soma + numero

print(f'\nMatriz:\n')

for i in range(3):
    for j in range(3):
        print(f'{matriz[i][j]} ', end="")

    print()

print(f'\nSoma dos elementos acima da diagonal principal: {soma}')
