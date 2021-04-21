custo_fabrica = float(input('Informe o custo de fábrica do carro: '))

custo_consumidor = 0

if custo_fabrica <= 12000.00:
    custo_consumidor = 1.05 * custo_fabrica
elif 12000.00 < custo_fabrica <= 25000.00:
    custo_consumidor = 1.25 * custo_fabrica
else:
    custo_consumidor = 1.35 * custo_fabrica

print(f'Custo para o consumidor: {custo_consumidor}')
