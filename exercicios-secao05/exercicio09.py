salario_trabalhador = float(input('Informe o valor do salário do trabalhador: '))
valor_prestacao = float(input('Informe o valor da prestação de um empréstimo: '))

if valor_prestacao > 0.20 * salario_trabalhador:
    print('Empréstimo não concedido')
else:
    print('Empréstimo concedido')
