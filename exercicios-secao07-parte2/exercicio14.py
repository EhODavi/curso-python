from random import randint

cartela = []
numeros_utilizados = []

for i in range(5):
    cartela.append([])

    for j in range(5):
        while True:
            numero = randint(0, 99)

            if numeros_utilizados.count(numero) == 0:
                cartela[i].append(numero)
                numeros_utilizados.append(numero)
                break

print('Cartela de bingo gerada:\n')

for i in range(5):
    for j in range(5):
        print(f'{cartela[i][j]} ', end="")

    print()
