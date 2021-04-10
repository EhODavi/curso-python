apostador1 = float(input('Informe o valor que o apostador 1 apostou: '))
apostador2 = float(input('Informe o valor que o apostador 2 apostou: '))
apostador3 = float(input('Informe o valor que o apostador 3 apostou: '))
valor_premio = float(input('Informe o valor do prêmio: '))

total_investido = apostador1 + apostador2 + apostador3
cotas = valor_premio / total_investido

print(f'Apostador 1: {apostador1 * cotas}')
print(f'Apostador 2: {apostador2 * cotas}')
print(f'Apostador 3: {apostador3 * cotas}')
