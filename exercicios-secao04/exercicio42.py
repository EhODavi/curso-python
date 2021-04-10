salario_base = float(input('Informe o salário base do funcionário: '))

gratificacao = 0.05 * salario_base
imposto = 0.07 * salario_base
salario = salario_base + gratificacao - imposto

print(f'Salário a receber: {salario}')
