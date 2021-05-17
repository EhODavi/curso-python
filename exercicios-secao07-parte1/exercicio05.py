numeros = []
quantidade_par = 0

for i in range(10):
    numero = int(input('Informe um número: '))
    numeros.append(numero)

    if numero % 2 == 0:
        quantidade_par = quantidade_par + 1

print(f'Vetor: {numeros}')
print(f'Quantidade de números pares: {quantidade_par}')
