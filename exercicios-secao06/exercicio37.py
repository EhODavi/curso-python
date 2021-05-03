for i in range(1000, 10000):
    numero = i
    digito1 = int(numero / 1000)
    numero = numero % 1000
    digito2 = int(numero / 100)
    numero = numero % 100
    digito3 = int(numero / 10)
    numero = numero % 10
    digito4 = numero

    if (digito1 * 10 + digito2 + digito3 * 10 + digito4) ** 2 == i:
        print(i)
