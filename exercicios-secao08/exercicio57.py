from typing import List


def soma_coluna(a: List[List[int]], n: int) -> int:
    soma: int = 0

    for i in range(7):
        soma += a[i][n]

    return soma
