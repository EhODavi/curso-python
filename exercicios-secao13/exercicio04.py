nome_arquivo = input('Informe o nome do arquivo: ')

with open(nome_arquivo) as arquivo:
    conteudo = arquivo.read()

    quantidade_vogal = 0
    quantidade_consoante = 0

    for letra in conteudo:
        if letra.lower() in ['a', 'e', 'i', 'o', 'u']:
            quantidade_vogal += 1
        elif letra.isalpha():
            quantidade_consoante += 1

    print(f"O arquivo '{nome_arquivo}' possui {quantidade_vogal} vogais e "
          f"{quantidade_consoante} consoantes!")
