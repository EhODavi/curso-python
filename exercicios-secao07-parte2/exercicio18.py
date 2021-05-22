matriz = []

for i in range(3):
    matriz.append([])

    for j in range(3):
        numero = int(input('Informe um número: '))
        matriz[i].append(numero)

array = []

for j in range(3):
    soma = 0

    for i in range(3):
        soma = soma + matriz[i][j]

    array.append(soma)

print(f'\nArray = {array}')
