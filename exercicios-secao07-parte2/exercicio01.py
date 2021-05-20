matriz = []
quantidade_maior = 0

for i in range(4):
    matriz.append([])

    for j in range(4):
        numero = int(input('Informe um número: '))
        matriz[i].append(numero)

        if numero > 10:
            quantidade_maior = quantidade_maior + 1

print('\nMatriz:\n')

for i in range(4):
    for j in range(4):
        print(f'{matriz[i][j]} ', end="")

    print()

print(f'\nQuantidade maior do que dez: {quantidade_maior}')
