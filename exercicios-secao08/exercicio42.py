from typing import List


def media(vetor: List[float]) -> float:
    soma: float = 0.0

    for numero in vetor:
        soma += numero

    return soma / len(vetor)
