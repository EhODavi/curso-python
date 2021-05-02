n = int(input('Informe n: '))
i = int(input('Informe i: '))
j = int(input('Informe j: '))

contador = 0
qtd_numeros = 0

while True:
    if qtd_numeros == n:
        break

    if contador % i == 0 or contador % j == 0:
        print(contador)
        qtd_numeros = qtd_numeros + 1

    contador = contador + 1
