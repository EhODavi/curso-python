from math import factorial, radians


def cos(graus: float) -> float:
    soma: float = 0.0
    x: float = radians(graus)

    for n in range(6):
        soma += (((-1) ** n) / factorial(2 * n)) * (x ** (2 * n))

    return soma
