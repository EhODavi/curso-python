from typing import List


def diagonal_secundaria(matriz: List[List[int]]) -> int:
    soma: int = 0

    for i in range(3):
        for j in range(3):
            if i + j == 2:
                soma += matriz[i][j]

    return soma
