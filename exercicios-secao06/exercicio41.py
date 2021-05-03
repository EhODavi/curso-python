while True:
    R1 = float(input('Informe a resistência do primeiro resistor: '))
    R2 = float(input('Informe a resistência do segundo resistor: '))

    if R1 == 0 or R2 == 0:
        break

    R = (R1 * R2) / (R1 + R2)

    print(f'A associação em paralelo dos resistores {R1} e {R2} terá resistência total de {R}')
