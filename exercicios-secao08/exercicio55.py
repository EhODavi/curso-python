from typing import List, Tuple


def soma_principal_secundaria(a: List[List[int]]) -> Tuple[int, int]:
    soma_principal: int = 0
    soma_secundaria: int = 0

    for i in range(3):
        for j in range(3):
            if i == j:
                if i == 1:
                    soma_secundaria += a[i][j]

                soma_principal += a[i][j]
            elif i + j == 2:
                soma_secundaria += a[i][j]

    return soma_principal, soma_secundaria
