valor_produto = float(input('Informe o valor do produto: '))
estado_destino = input('Informe o estado de destino: ')

if estado_destino == 'MG':
    print(f'Preço final do produto: {valor_produto * 1.07}')
elif estado_destino == 'SP':
    print(f'Preço final do produto: {valor_produto * 1.12}')
elif estado_destino == 'RJ':
    print(f'Preço final do produto: {valor_produto * 1.15}')
elif estado_destino == 'MS':
    print(f'Preço final do produto: {valor_produto * 1.08}')
else:
    print('ESTADO INVÁLIDO!')
