from typing import Tuple


def troque(a: float, b: float) -> Tuple[float, float]:
    aux: float = a
    a: float = b
    b: float = aux

    return a, b
