from math import factorial, radians


def cosh(graus: float) -> float:
    soma: float = 0.0
    x: float = radians(graus)

    for n in range(6):
        soma += (x ** (2 * n)) / factorial(2 * n)

    return soma
