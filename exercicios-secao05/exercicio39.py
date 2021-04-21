salario_atual = float(input('Informe o salário atual do funcionário: '))
tempo_servico = int(input('Informe o tempo de serviço do funcionário: '))

if salario_atual <= 500 and tempo_servico < 1:
    print(f'Novo salário: {salario_atual * 1.25}')
elif salario_atual <= 1000 and 1 <= tempo_servico <= 3:
    print(f'Novo salário: {salario_atual * 1.20 + 100}')
elif salario_atual <= 1500 and 4 <= tempo_servico <= 6:
    print(f'Novo salário: {salario_atual * 1.15 + 200}')
elif salario_atual <= 2000 and 7 <= tempo_servico <= 10:
    print(f'Novo salário: {salario_atual * 1.10 + 300}')
elif salario_atual > 2000 and tempo_servico > 10:
    print(f'Novo salário: {salario_atual + 500}')
else:
    print('O funcionário não tem direito a nenhum aumento')
