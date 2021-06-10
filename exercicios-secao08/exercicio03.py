def verifica_numero(numero: float) -> int:
    retorno: int

    if numero > 0:
        retorno = 1
    elif numero == 0:
        retorno = 0
    else:
        retorno = -1

    return retorno
