from typing import List


def quantidade_par(vetor: List[int]) -> int:
    contador: int = 0

    for numero in vetor:
        if numero % 2 == 0:
            contador += 1

    return contador
