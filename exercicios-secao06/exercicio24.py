numero = int(input('Informe um número inteiro: '))

soma_divisores = 0

for i in range(1, numero):
    if numero % i == 0:
        soma_divisores = soma_divisores + i

print(f'A soma de todos os divisores de {numero} é {soma_divisores}.')
