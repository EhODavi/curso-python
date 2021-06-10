def calcula_serie(n: int) -> float:
    soma: float = 0

    for i in range(1, n + 1):
        soma += ((i ** 2) + 1) / (i + 3)

    return soma
