v = []
v1 = []
v2 = []

for i in range(10):
    numero = int(input('Informe um número: '))
    v.append(numero)

    if numero % 2 == 0:
        v2.append(numero)
    else:
        v1.append(numero)

print(f'\nv = {v}')
print(f'v1 = {v1}')
print(f'v2 = {v2}')
