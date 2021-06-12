from typing import List


def uniao(vetor_a: List[int], vetor_b: List[int], vetor_c: List[int]) -> None:
    for i in range(10):
        if vetor_a[i] not in vetor_c:
            vetor_c.append(vetor_a[i])
        if vetor_b[i] not in vetor_c:
            vetor_c.append(vetor_b[i])
