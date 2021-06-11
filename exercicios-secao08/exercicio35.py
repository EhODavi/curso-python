from math import factorial


def fatorial_quadruplo(n: int) -> int:
    return factorial(2 * n) / factorial(n)
