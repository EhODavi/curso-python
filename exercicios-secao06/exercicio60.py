soma = 0
quantidade_numeros = 0
maior_numero = 0
menor_numero = 0
soma_par = 0
quantidade_par = 0

while True:
    numero = float(input('Informe um número: '))

    if numero == 0:
        break

    soma = soma + numero
    quantidade_numeros = quantidade_numeros + 1

    if quantidade_numeros == 1:
        maior_numero = numero
        menor_numero = numero

    if numero > maior_numero:
        maior_numero = numero
    if numero < menor_numero:
        menor_numero = numero

    if numero % 2 == 0:
        soma_par = soma_par + numero
        quantidade_par = quantidade_par + 1

if quantidade_numeros != 0:
    print(f'Soma dos números digitados: {soma}')
    print(f'Quantidade de números digitados: {quantidade_numeros}')
    print(f'Média dos números digitados: {soma / quantidade_numeros}')
    print(f'Maior número digitado: {maior_numero}')
    print(f'Menor número digitado: {menor_numero}')

    if quantidade_par != 0:
        print(f'Média dos números pares: {soma_par / quantidade_par}')
    else:
        print('Não foi informado nenhum número par!')
else:
    print('Não foi informado nenhum número!')
