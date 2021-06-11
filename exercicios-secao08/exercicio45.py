from typing import List


def desvio_padrao(v: List[float]) -> float:
    soma: float = 0.0

    for numero in v:
        soma += numero

    m: float = soma / len(v)

    desvio: float = 0.0

    for i in range(len(v)):
        desvio += ((v[i] - m) ** 2)

    desvio *= (1 / (len(v)))

    desvio = desvio ** (1 / 2)

    return desvio
