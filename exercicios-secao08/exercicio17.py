def soma_intervalo(a: int, b: int) -> int:
    soma: int = 0

    if a < b:
        for i in range(a + 1, b):
            soma += i
    else:
        for i in range(b + 1, a):
            soma += i

    return soma
