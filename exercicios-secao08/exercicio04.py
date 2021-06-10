def quadrado_perfeito(numero: int) -> bool:
    if numero > 0:
        raiz_quadrada = int(numero ** (1/2))

        if raiz_quadrada ** 2 == numero:
            return True

    return False
