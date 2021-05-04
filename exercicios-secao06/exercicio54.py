numero = int(input('Informe um número inteiro maior do que 1: '))

num_divisores = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        num_divisores = num_divisores + 1

if num_divisores == 2:
    print(f'O número {numero} é primo!')
else:
    print(f'O número {numero} não é primo!')
