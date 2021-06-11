def fatorial_duplo(n: int) -> int:
    fatorial: int = 1

    for i in range(1, n + 1, 2):
        fatorial *= i

    return fatorial
