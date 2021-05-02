numero1 = int(input('Informe o primeiro número: '))
numero2 = int(input('Informe o segundo número: '))

soma_par = 0
multiplicacao_impar = 1

if numero1 % 2 == 0:
    for i in range(numero1, numero2 + 1, 2):
        soma_par = soma_par + i
else:
    for i in range(numero1 + 1, numero2 + 1, 2):
        soma_par = soma_par + i

if numero1 % 2 == 0:
    for i in range(numero1 + 1, numero2 + 1, 2):
        multiplicacao_impar = multiplicacao_impar * i
else:
    for i in range(numero1, numero2 + 1, 2):
        multiplicacao_impar = multiplicacao_impar * i

print(f'A soma de todos os pares é: {soma_par}')
print(f'A multiplicação de todos os ímpares é: {multiplicacao_impar}')
