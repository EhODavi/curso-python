print('1 - ADIÇÃO')
print('2 - SUBTRAÇÃO')
print('3 - DIVISÃO')
print('4 - MULTIPLICAÇÃO')

opcao = int(input('INFORME A OPÇÃO DESEJADA: '))

numero1 = float(input('INFORME O PRIMEIRO NÚMERO: '))
numero2 = float(input('INFORME O SEGUNDO NÚMERO: '))

if opcao == 1:
    print(f'{numero1} + {numero2} = {numero1 + numero2}')
elif opcao == 2:
    print(f'{numero1} - {numero2} = {numero1 - numero2}')
elif opcao == 3:
    print(f'{numero1} / {numero2} = {numero1 / numero2}')
elif opcao == 4:
    print(f'{numero1} * {numero2} = {numero1 * numero2}')
