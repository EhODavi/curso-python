from math import factorial


def soma_fatorial(n: int) -> int:
    soma: int = 0
    fatorial_str: str = str(factorial(n))

    for letra in fatorial_str:
        soma += int(letra)

    return soma
