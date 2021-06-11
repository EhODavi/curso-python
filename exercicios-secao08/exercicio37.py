def hiper_fatorial(n: int) -> int:
    produtorio: int = 1

    for k in range(1, n + 1):
        produtorio *= (k ** k)

    return produtorio
