from typing import List


def transposta(matriz: List[List[int]]) -> List[List[int]]:
    matriz_transposta: List[List[int]] = []

    for i in range(len(matriz)):
        matriz_transposta.append([])

        for j in range(len(matriz)):
            matriz_transposta[i].append(matriz[j][i])

    return matriz_transposta
