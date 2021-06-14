with open('arq.txt', 'w') as arquivo:
    while True:
        caractere = input('Informe um caractere (O para terminar): ')

        if caractere == 'O':
            break

        arquivo.write(caractere + '\n')

print('\nConteúdo do arquivo:')

with open('arq.txt') as arquivo:
    linhas = arquivo.readlines()

    for linha in linhas:
        print(linha, end='')
