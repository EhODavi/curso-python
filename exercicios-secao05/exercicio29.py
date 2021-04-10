import random

acertos = 0

for i in range(5):
    a = random.randint(1, 100)
    b = random.randint(1, 100)

    resultado = int(input(f'{a} + {b} = '))

    if resultado == (a + b):
        print('ACERTOU!')
        acertos = acertos + 1
    else:
        print('ERROU!')
        print(f'{a} + {b} = {a + b}')

print(f'ACERTOS: {acertos}')
