numeros = []

for i in range(8):
    numero = float(input('Informe um número: '))
    numeros.append(numero)

X = int(input('Informe o valor de X: '))
Y = int(input('Informe o valor de Y: '))

print(f'{numeros[X]} + {numeros[Y]} = {numeros[X] + numeros[Y]}')
