import random

numero_aleatorio = random.randint(1, 1000)
tentativas = 0

while True:
    numero = int(input('TENTE ADIVINHAR O NÚMERO ALEATÓRIO: '))

    tentativas = tentativas + 1

    if numero == numero_aleatorio:
        print(f'\nACERTOU EM {tentativas} TENTATIVAS!\n')
        break
    elif numero < numero_aleatorio:
        print('\nMAIOR!\n')
    else:
        print('\nMENOR!\n')
