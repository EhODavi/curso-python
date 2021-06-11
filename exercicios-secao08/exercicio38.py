def fatorial_exponensial(n: int) -> int:
    base: int = 1
    expoente: int = 0

    while base != n + 1:
        expoente = base ** expoente
        base += 1

    return expoente
