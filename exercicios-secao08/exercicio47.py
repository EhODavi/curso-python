from typing import List


def maior_dez(matriz: List[List[int]]) -> int:
    quantidade: int = 0

    for i in range(4):
        for j in range(4):
            if matriz[i][j] > 10:
                quantidade += 1

    return quantidade
