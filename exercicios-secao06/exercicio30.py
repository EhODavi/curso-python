n = int(input('Informe o valor de n: '))

soma1 = 0
soma2 = 0
soma3 = 0

for i in range(1, n + 1):
    soma1 = soma1 + i

for i in range(1, 2 * n):
    if i % 2 == 0:
        soma2 = soma2 - i
    else:
        soma2 = soma2 + i

for i in range(1, 2 * n, 2):
    soma3 = soma3 + i

print(f'Primeira soma: {soma1}')
print(f'Segunda soma: {soma2}')
print(f'Terceira soma: {soma3}')
