from typing import List


def acima_diagonal_principal(matriz: List[List[int]]) -> int:
    soma: int = 0

    for i in range(3):
        for j in range(3):
            if j > i:
                soma += matriz[i][j]

    return soma
