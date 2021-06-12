def ler(p):
    for i in range(5):
        if i != 0:
            print()

        sexo = input('Informe o sexo (M - Masculino ou F - Feminino): ')
        olhos = input('Informe a cor dos olhos (A - Azuis ou C - Castanhos): ')
        cabelos = input('Informe a cor dos cabelos (L - Louros, P - Pretos ou C - Castanhos): ')
        idade = int(input('Informe a idade: '))

        p.append((sexo, olhos, cabelos, idade))


def media(pe):
    soma_idade = 0
    quantidade_pessoas = 0

    for i in range(5):
        if pe[i][1] == 'C' and pe[i][2] == 'P':
            soma_idade += pe[i][3]
            quantidade_pessoas += 1

    if quantidade_pessoas != 0:
        return soma_idade / quantidade_pessoas

    return 'Nenhuma pessoa possui olhos castanhos e cabelos pretos!'


def maior_idade(pe):
    maior = pe[0][3]

    for i in range(1, 5):
        if pe[i][3] > maior:
            maior = pe[i][3]

    return maior


def quantidade(pe):
    quantidade_pessoas = 0

    for i in range(5):
        if pe[i][0] == 'F' and 18 <= pe[i][3] <= 35 and pe[i][1] == 'A' and pe[i][2] == 'L':
            quantidade_pessoas += 1

    return quantidade_pessoas


pessoas = []

ler(pessoas)

print(f'\nA média de idade das pessoas com olhos castanhos e cabelos pretos é: {media(pessoas)}')
print(f'A maior idade entre os habitantes é: {maior_idade(pessoas)}')
print(f'A quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35 (inclusive) '
      f'e que tenham olhos azuis e cabelos louros: {quantidade(pessoas)}')
