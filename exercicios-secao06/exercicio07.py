soma = 0
contador = 0

while contador < 10:
    numero = int(input(f'Informe o {contador + 1}º número: '))

    if numero > 0:
        soma = soma + numero
        contador = contador + 1

media = soma / 10

print(f'A média de todos os números informados é: {media}')
