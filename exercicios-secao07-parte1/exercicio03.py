numeros = []
numeros_quadrado = []

for i in range(10):
    numero = float(input('Informe um número: '))
    numeros.append(numero)
    numeros_quadrado.append(numero ** 2)

print(f'Números: {numeros}')
print(f'Números ao quadrado: {numeros_quadrado}')
