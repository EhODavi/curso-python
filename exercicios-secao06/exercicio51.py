ano_atual = int(input('Informe o ano atual: '))

salario = 2000.00
aumento = 1.5

for i in range(1996, ano_atual + 1):
    salario = salario * (1 + aumento / 100)
    aumento = aumento * 2

print(f'Salário atual: {salario}')
