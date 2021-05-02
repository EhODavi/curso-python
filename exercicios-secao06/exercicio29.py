soma = 0.0
fatorial = 2

for i in range(1, 5):
    soma = soma + (i / fatorial)
    fatorial = fatorial * (2*i + 1) * (2*i + 2)

print(f'Soma: {soma}')
