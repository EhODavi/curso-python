def calcular(numero1: float, numero2: float, simbolo: str) -> float:
    resultado: float

    if simbolo == '+':
        resultado = numero1 + numero2
    elif simbolo == '-':
        resultado = numero1 - numero2
    elif simbolo == '/':
        resultado = numero1 / numero2
    elif simbolo == '*':
        resultado = numero1 * numero2

    return resultado
