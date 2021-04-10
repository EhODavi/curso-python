base_maior = float(input('Informe a base maior do trapézio: '))
base_menor = float(input('Informe a base menor do trapézio: '))
altura = float(input('Informe a altura do trapézio: '))

if base_maior > 0 and base_menor > 0 and altura > 0:
    area = ((base_maior + base_menor) * altura) / 2
    print(f'Área do trapézio: {area}')
