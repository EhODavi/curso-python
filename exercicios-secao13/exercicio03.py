nome_arquivo = input('Informe o nome do arquivo: ')

with open(nome_arquivo) as arquivo:
    conteudo = arquivo.read()
    
    quantidade = 0

    for letra in conteudo:
        if letra.lower() in ['a', 'e', 'i', 'o', 'u']:
            quantidade += 1

    print(f"O arquivo '{nome_arquivo}' possui {quantidade} vogais!")
