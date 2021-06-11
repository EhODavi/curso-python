from typing import List
from random import randint


def gera_vetor(vetor: List[int]) -> None:
    tamanho_vetor: int = 0

    while tamanho_vetor != 5:
        while True:
            numero_sorteado: int = randint(1, 10)

            if numero_sorteado not in vetor:
                vetor.append(numero_sorteado)
                tamanho_vetor += 1
                break
