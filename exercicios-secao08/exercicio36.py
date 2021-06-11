from math import factorial


def superfatorial(n: int) -> int:
    produtorio: int = 1

    for i in range(1, n + 1):
        produtorio *= factorial(i)

    return produtorio
