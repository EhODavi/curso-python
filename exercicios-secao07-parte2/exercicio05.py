matriz = []

for i in range(5):
    matriz.append([])

    for j in range(5):
        numero = int(input('Informe um número: '))

        matriz[i].append(numero)

X = int(input('\nInforme o valor de X: '))

encontrei = False

for i in range(5):
    for j in range(5):
        if X == matriz[i][j]:
            print(f'\nO valor {X} está na linha {i} e coluna {j}!')
            encontrei = True
            break

    if encontrei:
        break

if not encontrei:
    print(f'\nO valor {X} não foi encontrado!')
