from typing import List


def separa_vetor(vetor_x: List[int], vetor_a: List[int], vetor_b: List[int]) -> None:
    for i in range(len(vetor_x)):
        if vetor_x[i] % 2 == 0:
            vetor_a.append(vetor_x[i])
        else:
            vetor_b.append(vetor_x[i])
