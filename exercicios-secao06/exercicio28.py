N = int(input('Informe um valor N inteiro e positivo: '))

soma = 1.0
fatorial = 1

for i in range(1, N + 1):
    fatorial = fatorial * i
    soma = soma + (1 / fatorial)

print(f'E = {soma}')
