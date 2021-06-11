from typing import List


def maior(vetor: List[int]) -> int:
    maior_valor = vetor[0]

    for numero in vetor:
        if numero > maior_valor:
            maior_valor = numero

    return maior_valor
