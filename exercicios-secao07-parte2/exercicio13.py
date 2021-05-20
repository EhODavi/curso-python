from random import randint

matriz = []

for i in range(4):
    matriz.append([])

    for j in range(4):
        matriz[i].append(randint(1, 20))

matriz_triangular_inferior = []

for i in range(4):
    matriz_triangular_inferior.append([])

    for j in range(4):
        if j > i:
            matriz_triangular_inferior[i].append(0)
        else:
            matriz_triangular_inferior[i].append(matriz[i][j])

print(f'Matriz:\n')

for i in range(4):
    for j in range(4):
        print(f'{matriz[i][j]} ', end="")

    print()

print(f'\nMatriz triangular inferior:\n')

for i in range(4):
    for j in range(4):
        print(f'{matriz_triangular_inferior[i][j]} ', end="")

    print()
