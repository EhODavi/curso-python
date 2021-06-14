nome_arquivo = input('Informe o nome do arquivo: ')

ocorrencias = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0,
               'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0,
               'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0,
               'y': 0, 'z': 0}

with open(nome_arquivo) as arquivo:
    conteudo = arquivo.read()

    for letra in conteudo:
        if letra.isalpha():
            ocorrencias[letra.lower()] += 1

print('\nNúmero de vezes que cada letra aparece no arquivo: ')
for chave, valor in ocorrencias.items():
    print(f'{chave} = {valor}')
