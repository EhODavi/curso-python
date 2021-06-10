def soma_algarismos(numero):
    if numero > 0:
        numero_str: str = str(numero)
        soma = 0

        for algarismo in numero_str:
            soma += int(algarismo)

        return soma
    return 'Número inválido'
