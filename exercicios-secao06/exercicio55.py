n = int(input('Informe um número inteiro não negativo n: '))

soma = 0
numero = 2
num_primos = 0

while True:
    num_divisores = 0

    for i in range(1, numero + 1):
        if numero % i == 0:
            num_divisores = num_divisores + 1

    if num_divisores == 2:
        num_primos = num_primos + 1
        soma = soma + numero

        if num_primos == n:
            break

    numero = numero + 1

print(f'Soma: {soma}')
