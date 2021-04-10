a = float(input('Informe o valor de "a": '))
b = float(input('Informe o valor de "b": '))
c = float(input('Informe o valor de "c": '))

if a != 0:
    delta = b ** 2 - 4 * a * c

    if delta < 0:
        print('NÃO EXISTE RAIZ!')
    elif delta == 0:
        x = -b / (2 * a)
        print(f'RAIZ ÚNICA | RAIZ: {x}')
    else:
        x1 = (-b + delta ** 0.5) / (2 * a)
        x2 = (-b - delta ** 0.5) / (2 * a)
        print(f'PRIMEIRA RAIZ: {x1}')
        print(f'SEGUNDA RAIZ: {x2}')
else:
    print('NÃO É EQUAÇÃO DO SEGUNDO GRAU!')
