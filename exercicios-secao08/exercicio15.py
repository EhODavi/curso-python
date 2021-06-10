def eh_triangulo(a: float, b: float, c: float) -> bool:
    if a > 0 and b > 0 and c > 0 and a < (b + c) and b < (a + c) and c < (a + b):
        return True

    return False


def tipo_triangulo(a: float, b: float, c: float) -> None:
    if eh_triangulo(a, b, c):
        if a == b == c:
            print('Triângulo Equilátero!')
        elif a == b or a == c or b == c:
            print('Triângulo Isósceles!')
        else:
            print('Triângulo Escaleno!')
    else:
        print('Não é um Triângulo!')
