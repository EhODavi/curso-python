num_habitantes = int(input('Informe o número de habitantes da cidade: '))
valor_kwh = float(input('Informe o valor do kwh: '))

menor_consumo = 0
maior_consumo = 0
soma_consumo = 0
soma_consumo1 = 0
soma_consumo2 = 0
soma_consumo3 = 0

for i in range(num_habitantes):
    print(f'\nHabitante {i + 1}:')
    consumo_mes = float(input('Informe o consumo do mês: '))
    codigo_consumidor = int(input('Informe o código do consumidor (1 - Residencial, 2 - Comercial, 3- Industrial): '))

    soma_consumo = soma_consumo + consumo_mes

    if codigo_consumidor == 1:
        soma_consumo1 = soma_consumo1 + consumo_mes
    elif codigo_consumidor == 2:
        soma_consumo2 = soma_consumo2 + consumo_mes
    elif codigo_consumidor == 3:
        soma_consumo3 = soma_consumo3 + consumo_mes

    if i == 0:
        maior_consumo = consumo_mes
        menor_consumo = consumo_mes
    if consumo_mes > maior_consumo:
        maior_consumo = consumo_mes
    if consumo_mes < menor_consumo:
        menor_consumo = consumo_mes

print(f'\nMaior consumo: {maior_consumo}')
print(f'Menor consumo: {menor_consumo}')
print(f'Média do consumo: {soma_consumo / num_habitantes}')
print(f'Soma do consumo (1 - Residencial): {soma_consumo1}')
print(f'Soma do consumo (2 - Comercial): {soma_consumo2}')
print(f'Soma do consumo (3 - Industrial): {soma_consumo3}')
