from typing import Tuple


def simplifica(numerador: int, denominador: int) -> Tuple[int, int]:
    menor: int = min(numerador, denominador)

    for i in range(menor, 1, -1):
        if numerador % i == 0 and denominador % i == 0:
            numerador /= i
            denominador /= i
            break

    return int(numerador), int(denominador)
