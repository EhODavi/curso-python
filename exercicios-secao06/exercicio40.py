maior_numero = -1
menor_numero = -1

while True:
    numero = int(input('Informe um número: '))

    if numero < 0:
        if maior_numero >= 0 and menor_numero >= 0:
            print(f'Maior número: {maior_numero}')
            print(f'Menor número: {menor_numero}')
        break

    if maior_numero < 0 and menor_numero < 0:
        maior_numero = numero
        menor_numero = numero
    else:
        if numero > maior_numero:
            maior_numero = numero
        if numero < menor_numero:
            menor_numero = numero
