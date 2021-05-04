n = int(input('Informe um número inteiro positivo n: '))

numero = 1
qtd_por_linha = 1

for i in range(n):
    for j in range(qtd_por_linha):
        print(f'{numero} ', end="")
        numero = numero + 1

    print()
    qtd_por_linha = qtd_por_linha + 1
