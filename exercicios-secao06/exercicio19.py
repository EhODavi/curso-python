numero = int(input('Informe um número inteiro entre 100 e 999: '))

divisor = 100

for i in range(3):
    print(int(numero / divisor))
    numero = int(numero % divisor)
    divisor = divisor / 10
