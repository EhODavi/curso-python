from typing import List


def soma_linha(a: List[List[int]], n: int) -> int:
    soma: int = 0

    for j in range(6):
        soma += a[n][j]

    return soma
