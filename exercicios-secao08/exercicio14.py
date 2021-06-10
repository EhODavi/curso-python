def avalia_carro(distancia: float, litros: float) -> None:
    consumo_por_litro: float = distancia / litros

    if consumo_por_litro < 8:
        print('Venda o carro!')
    elif 8 <= consumo_por_litro <= 12:
        print('Econômico!')
    else:
        print('Super econômico!')
