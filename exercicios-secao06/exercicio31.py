S = 0.0
numerador = 1
denominador = 1

while numerador != 101 and denominador != 51:
    S = S + numerador / denominador
    numerador = numerador + 2
    denominador = denominador + 1

print(f'S = {S}')
