vetor = []

for i in range(10):
    numero = int(input(f'Informe o {i + 1}-ésimo número: '))
    vetor.append(numero)

with open('novo_arquivo.txt', 'w') as saida:
    for numero in vetor:
        saida.write(str(format(numero, 'b')) + '\n')
