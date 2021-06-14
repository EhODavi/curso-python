nome_arquivo = input('Informe o nome do arquivo: ')
caractere = input('Informe um caractere: ')

with open(nome_arquivo) as arquivo:
    conteudo = arquivo.read()

    quantidade_caractere = 0

    for letra in conteudo:
        if letra == caractere:
            quantidade_caractere += 1

    print(f"O caractere '{caractere}' aparece {quantidade_caractere} vezes no arquivo '{nome_arquivo}'!")
