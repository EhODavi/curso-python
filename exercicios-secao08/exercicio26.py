def somatorio(n: int) -> int:
    soma: int = 0

    for i in range(1, n + 1):
        soma += i

    return soma
