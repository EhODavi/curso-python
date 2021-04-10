numero = input('Insira um número inteiro maior do que zero: ')

if int(numero) > 0:
    soma = 0
    for elemento in numero:
        soma = int(elemento) + soma

    print(f'A soma de todos os algarismos do número {numero} é {soma}!')
else:
    print('NÚMERO INVÁLIDO!')
