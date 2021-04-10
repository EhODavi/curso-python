numero = int(input('Informe um número inteiro: '))

if (numero % 3 == 0 or numero % 5 == 0) and not (numero % 3 == 0 and numero % 5 == 0):
    print(f'O número {numero} é divisível por 3 ou 5, mas não simultaneamente pelos dois')
