codigo_produto = int(input('Informe o código do produto: '))
quantidade = int(input('Informe a quantidade: '))

if codigo_produto == 100:
    print('Cachorro Quente - 100')
    print(f'Total à pagar: {quantidade} x 1.20 = {quantidade * 1.20}')
elif codigo_produto == 101:
    print('Bauru Simples - 101')
    print(f'Total à pagar: {quantidade} x 1.30 = {quantidade * 1.30}')
elif codigo_produto == 102:
    print('Bauru com Ovo - 102')
    print(f'Total à pagar: {quantidade} x 1.50 = {quantidade * 1.50}')
elif codigo_produto == 103:
    print('Hamburguer - 103')
    print(f'Total à pagar: {quantidade} x 1.20 = {quantidade * 1.20}')
elif codigo_produto == 104:
    print('Cheeseburguer - 104')
    print(f'Total à pagar: {quantidade} x 1.70 = {quantidade * 1.70}')
elif codigo_produto == 105:
    print('Suco - 105')
    print(f'Total à pagar: {quantidade} x 2.20 = {quantidade * 2.20}')
elif codigo_produto == 106:
    print('Refrigerante - 106')
    print(f'Total à pagar: {quantidade} x 1.00 = {quantidade * 1.00}')
