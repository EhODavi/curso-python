contador = 0
num_pares = 0

while True:
    numero = int(input('Informe um número: '))

    if numero == 1000:
        break

    if numero % 2 == 0:
        num_pares = num_pares + 1

    contador = contador + 1

print(f'Qunatidade de números informados: {contador}')
print(f'Quantidade de números pares: {num_pares}')
