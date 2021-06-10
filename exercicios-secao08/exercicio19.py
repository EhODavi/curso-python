def eh_primo(numero: int) -> bool:
    quantidade_divisores: int = 0

    for i in range(1, numero + 1):
        if numero % i == 0:
            quantidade_divisores += 1

    if quantidade_divisores == 2:
        return True

    return False


def maior_fator_primo(numero: int) -> int:
    for i in range(numero, 1, -1):
        if eh_primo(i) and numero % i == 0:
            return i
