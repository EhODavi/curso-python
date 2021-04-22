qtd_multiplo = 0
contador = 1

while True:
    if contador % 3 == 0:
        print(contador)
        qtd_multiplo = qtd_multiplo + 1
    if qtd_multiplo == 5:
        break
    contador = contador + 1
