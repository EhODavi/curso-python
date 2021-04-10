numero1 = float(input('Informe o primeiro número: '))
numero2 = float(input('Informe o segundo número: '))

if numero1 > numero2:
    print(f'O maior número é o primeiro ({numero1})!')
elif numero1 == numero2:
    print('Os dois números são iguais!')
else:
    print(f'O maior número é o segundo ({numero2})!')
