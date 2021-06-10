from math import factorial, radians


def sin(graus: float) -> float:
    soma: float = 0.0
    x: float = radians(graus)

    for i in range(6):
        soma += ((-1) ** i) * (x ** (2 * i + 1)) / (factorial(2 * i + 1))

    return soma
