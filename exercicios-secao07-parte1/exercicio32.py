x = []
y = []

print('Preenchendo o vetor x:\n')

for i in range(5):
    numero = int(input('Informe um número: '))
    x.append(numero)

print('\nPreenchendo o vetor y:\n')

for i in range(5):
    numero = int(input('Informe um número: '))
    y.append(numero)

a = []
b = []
c = []
d = []
e = []

for i in range(5):
    a.append(x[i] + y[i])
    b.append(x[i] * y[i])

    if y.count(x[i]) == 0:
        c.append(x[i])

    if y.count(x[i]) > 0:
        d.append(x[i])

    if e.count(x[i]) == 0:
        e.append(x[i])

    if e.count(y[i]) == 0:
        e.append(y[i])

print(f'\nx = {x}')
print(f'y = {y}')
print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')
print(f'd = {d}')
print(f'e = {e}')
