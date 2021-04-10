altura = float(input('Informe a altura: '))
peso = float(input('Informe o peso: '))

if altura < 1.20 and peso <= 60:
    print('Classificação: A')
elif altura < 1.20 and 60 < peso <= 90:
    print('Classificação: D')
elif altura < 1.20 and peso > 90:
    print('Classificação: G')
elif 1.20 <= altura <= 1.70 and peso <= 60:
    print('Classificação: B')
elif 1.20 <= altura <= 1.70 and 60 < peso <= 90:
    print('Classificação: E')
elif 1.20 <= altura <= 1.70 and peso > 90:
    print('Classificação: H')
elif altura > 1.70 and peso <= 60:
    print('Classificação: C')
elif altura > 1.70 and 60 < peso <= 90:
    print('Classificação: F')
elif altura > 1.70 and peso > 90:
    print('Classificação: I')
