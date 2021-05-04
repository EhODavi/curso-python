salario_carlos = float(input('Informe o salário do Carlos: '))
taxa_carlos = 2
salario_joao = salario_carlos / 3
taxa_joao = 5
meses = 0

while salario_joao < salario_carlos:
    salario_carlos = salario_carlos * (1 + taxa_carlos / 100)
    salario_joao = salario_joao * (1 + taxa_joao / 100)
    meses = meses + 1

print(f'Meses: {meses}')
