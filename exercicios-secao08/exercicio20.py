def fatorial(n: int) -> int:
    resultado: int = 1

    for i in range(1, n + 1):
        resultado *= i

    return resultado
