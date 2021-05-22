tabuleiro = []

print('Informe o tabuleiro atual:')

for i in range(3):
    tabuleiro.append([])

    for j in range(3):
        numero = int(input())
        tabuleiro[i].append(numero)

print('\nTabuleiro antes:\n')

for i in range(3):
    for j in range(3):
        print(f'{tabuleiro[i][j]} ', end="")
    print()

soma_eu = []
soma_adversario = []

for i in range(3):
    soma_eu.append(0)
    soma_adversario.append(0)

    for j in range(3):
        if tabuleiro[i][j] == -1:
            soma_eu[i] = soma_eu[i] + 1
        elif tabuleiro[i][j] == 1:
            soma_adversario[i] = soma_adversario[i] + 1

for j in range(3):
    soma_eu.append(0)
    soma_adversario.append(0)

    for i in range(3):
        if tabuleiro[i][j] == -1:
            soma_eu[j + 3] = soma_eu[j + 3] + 1
        elif tabuleiro[i][j] == 1:
            soma_adversario[j + 3] = soma_adversario[j + 3] + 1

soma_eu.append(0)
soma_adversario.append(0)

for i in range(3):
    if tabuleiro[i][i] == -1:
        soma_eu[6] = soma_eu[6] + 1
    elif tabuleiro[i][i] == 1:
        soma_adversario[6] = soma_adversario[6] + 1

soma_eu.append(0)
soma_adversario.append(0)

for i in range(3):
    if tabuleiro[i][2 - i] == -1:
        soma_eu[7] = soma_eu[7] + 1
    elif tabuleiro[i][2 - i] == 1:
        soma_adversario[7] = soma_adversario[7] + 1

maior = 0
posicao_maior = 0

for i in range(8):
    if soma_eu[i] + soma_adversario[i] < 3:
        if soma_eu[i] >= maior:
            maior = soma_eu[i]
            posicao_maior = i
        if soma_adversario[i] > maior:
            maior = soma_adversario[i]
            posicao_maior = i

if posicao_maior <= 2:
    linha = posicao_maior

    for j in range(3):
        if tabuleiro[linha][j] == 0:
            tabuleiro[linha][j] = -1
            break
elif 3 <= posicao_maior <= 5:
    coluna = posicao_maior - 3

    for i in range(3):
        if tabuleiro[i][coluna] == 0:
            tabuleiro[i][coluna] = -1
            break
elif posicao_maior == 6:
    for i in range(3):
        if tabuleiro[i][i] == 0:
            tabuleiro[i][i] = -1
            break
else:
    for i in range(3):
        if tabuleiro[i][2 - i] == 0:
            tabuleiro[i][2 - i] = -1
            break

print('\nTabuleiro depois:\n')

for i in range(3):
    for j in range(3):
        print(f'{tabuleiro[i][j]} ', end="")
    print()
