from typing import List


def soma(a: List[List[int]]) -> int:
    s: int = 0

    for i in range(4):
        for j in range(4):
            s += a[i][j]

    return s
