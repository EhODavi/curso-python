import random

n = int(input('Informe a quantidade de lançamentos: '))

for i in range(n):
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)

    print(f'Dado 1 = {dado1}')
    print(f'Dado 2 = {dado2}')

    if dado1 < dado2:
        print('Dado 1 < Dado 2\n')
    elif dado1 == dado2:
        print('Dado 1 = Dado 2\n')
    else:
        print('Dado 1 > Dado 2\n')
