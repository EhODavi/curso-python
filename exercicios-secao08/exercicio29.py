from math import factorial, radians


def sinh(graus: float) -> float:
    soma: float = 0.0
    x: float = radians(graus)

    for n in range(6):
        soma += (x ** (2 * n + 1)) / factorial(2 * n + 1)

    return soma
