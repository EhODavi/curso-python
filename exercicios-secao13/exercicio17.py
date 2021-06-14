arquivo_entrada = input('Informe o nome do arquivo de entrada: ')

with open(arquivo_entrada) as entrada, open('matriz_saida.txt', 'w') as saida:
    linha_arquivo = entrada.readline()
    linha_arquivo = linha_arquivo.split(' ')
    linha = int(linha_arquivo[0])
    coluna = int(linha_arquivo[1])
    posicao = int(linha_arquivo[2])

    posicoes = []

    for i in range(posicao):
        linha_arquivo = entrada.readline()
        linha_arquivo = linha_arquivo.split(' ')
        posicoes.append((int(linha_arquivo[0]), int(linha_arquivo[1])))

    matriz = []

    for i in range(linha):
        matriz.append([])

        for j in range(coluna):
            matriz[i].append(1)

    for i in range(posicao):
        matriz[posicoes[i][0]][posicoes[i][1]] = 0

    for i in range(linha):
        for j in range(coluna):
            if j == coluna - 1:
                saida.write(str(matriz[i][j]))
            else:
                saida.write(str(matriz[i][j]) + ' ')

        if i != linha - 1:
            saida.write('\n')
