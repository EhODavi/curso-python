valor_hora = float(input('Informe o valor (em reais) da hora de trabalho: '))
num_horas = float(input('Informe a quantidade de horas trabalhadas no mês: '))

valor_pago = 1.10 * (valor_hora * num_horas)

print(f'Valor a ser pago: {valor_pago}')
