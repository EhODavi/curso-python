distancia = float(input('Informe a distância em km: '))
gasolina = float(input('Informe a quantidade de litros de gasolina consumidos por um carro em um percurso: '))

consumo = distancia / gasolina

if consumo < 8:
    print('VENDA O CARRO!')
elif 8 <= consumo <= 14:
    print('ECONÔMICO!')
else:
    print('SUPER ECONÔMICO!')
