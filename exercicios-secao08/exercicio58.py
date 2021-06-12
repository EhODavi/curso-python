from typing import List


def multiplica(a: List[List[int]], b: List[List[int]], c: List[List[int]]) -> None:
    for i in range(len(a)):
        c.append([])

        for j in range(len(a)):
            soma: int = 0

            for k in range(len(a)):
                soma += a[i][k] * b[k][j]

            c[i].append(soma)

    return c
