n = int(input('Informe um número inteiro e positivo: '))

soma = 0.0

for i in range(1, n + 1):
    soma = soma + (1 / i)

print(f'H(n) = {soma}')
