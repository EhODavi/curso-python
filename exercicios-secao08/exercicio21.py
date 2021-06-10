def eh_primo(numero: int) -> bool:
    quantidade_divisores: int = 0

    for i in range(1, numero + 1):
        if numero % i == 0:
            quantidade_divisores += 1

    if quantidade_divisores == 2:
        return True

    return False


def quantidade_primos(n: int) -> int:
    qtd: int = 0

    for i in range(2, n):
        if eh_primo(i):
            qtd += 1

    return qtd
