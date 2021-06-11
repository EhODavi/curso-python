from typing import List


def imprime(v: List[float]) -> None:
    print(v)


def imprime_invertido(v: List[float]) -> None:
    print(v[::-1])


def media(v: List[float]) -> float:
    return sum(v) / len(v)
