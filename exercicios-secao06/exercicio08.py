numero = float(input('Informe um número: '))
maior_numero = numero
menor_numero = numero

for i in range(9):
    numero = float(input('Informe um número: '))

    if numero < menor_numero:
        menor_numero = numero
    if numero > maior_numero:
        maior_numero = numero

print(f'Maior número: {maior_numero}')
print(f'Menor número: {menor_numero}')
