from typing import List


def eh_identidade(matriz: List[List[int]]) -> bool:
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if (i == j and matriz[i][j] != 1) or (i != j and matriz[i][j] != 0):
                return False

    return True
