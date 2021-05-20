matriz = []

for i in range(4):
    matriz.append([])

    for j in range(4):
        matriz[i].append(i * j)

for i in range(4):
    for j in range(4):
        print(f'{matriz[i][j]} ', end="")

    print()
