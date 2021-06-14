arquivo_entrada = input('Informe o nome do arquivo de entrada: ')

with open(arquivo_entrada) as entrada:
    linhas = entrada.readlines()
    preco_total = 0.0

    for linha in linhas:
        preco = linha.split(';')[1]

        preco_total += float(preco)

    print(f'Preço total da compra: {preco_total:.2f}')
