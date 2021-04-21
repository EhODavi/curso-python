preco_antigo = float(input('Informe o preço antigo do produto: '))
preco_novo = preco_antigo

if preco_novo <= 50:
    preco_novo = preco_novo * 1.05
elif 50 < preco_novo <= 100:
    preco_novo = preco_novo * 1.10
else:
    preco_novo = preco_novo * 1.15

print(f'Preço novo: {preco_novo}')

if preco_novo <= 80:
    print('Barato')
elif 80 < preco_novo <= 120:
    print('Normal')
elif 120 < preco_novo <= 200:
    print('Caro')
else:
    print('Muito caro')
