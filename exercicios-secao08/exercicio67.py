from typing import List


def getchar() -> str:
    caractere: str = input()

    return caractere


def rotina(vetor: List[str], tamanho: int) -> None:
    for _ in range(tamanho):
        valor: str = getchar()

        if valor != '':
            vetor.append(valor)
        else:
            break

    print(vetor)
