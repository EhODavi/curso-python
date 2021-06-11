from math import factorial


def neperiaro(termos: int) -> float:
    soma: float = 0.0

    for n in range(termos):
        soma += 1 / factorial(n)

    return soma
