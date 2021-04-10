print('Escolha a opção:')
print('1- Soma de 2 números.')
print('2- Diferença entre 2 números (maior pelo menor).')
print('3- Produto entre 2 números.')
print('4- Divisão entre 2 números (o denominador não pode ser zero).')
opcao = int(input('Opção'))

numero1 = float(input('Informe o primeiro número: '))
numero2 = float(input('Informe o segundo número: '))

if opcao == 1:
    print(f'{numero1} + {numero2} = {numero1 + numero2}')
elif opcao == 2:
    if numero1 >= numero2:
        print(f'{numero1} - {numero2} = {numero1 - numero2}')
    else:
        print('MAIOR PELO MENOR!')
elif opcao == 3:
    print(f'{numero1} * {numero2} = {numero1 * numero2}')
elif opcao == 4:
    if numero2 != 0:
        print(f'{numero1} / {numero2} = {numero1 / numero2}')
    else:
        print('DENOMINADOR IGUAL A ZERO!')
else:
    print('OPÇÃO INVÁLIDA!')
