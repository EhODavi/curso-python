numero1 = 0
numero2 = 1
soma = 0

while True:
    numero3 = numero1 + numero2

    if numero3 > 4000000:
        break

    if numero3 % 2 == 0:
        soma = soma + numero3

    numero1 = numero2
    numero2 = numero3

print(f'Soma: {soma}')
