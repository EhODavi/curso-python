vetor = []
tamanho_vetor = 0
contador = 0

while True:
    contador_str = str(contador)
    contador_str_len = len(contador_str)

    if contador % 7 != 0 or contador_str[contador_str_len - 1] == '7':
        vetor.append(contador)
        tamanho_vetor = tamanho_vetor + 1

    if tamanho_vetor == 100:
        break

    contador = contador + 1

print(f'Vetor: {vetor}')
