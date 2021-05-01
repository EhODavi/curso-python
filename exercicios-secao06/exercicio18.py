N = int(input('Informe a quantidade de números que serão informados: '))

maior_numero = float(input('Informe um número: '))
qtd_maior = 1

for i in range(N - 1):
    numero = float(input('Informe um número: '))

    if numero > maior_numero:
        maior_numero = numero
        qtd_maior = 1
    elif numero == maior_numero:
        qtd_maior = qtd_maior + 1

print(f'O maior número ({maior_numero}) foi informado {qtd_maior} vezes')
