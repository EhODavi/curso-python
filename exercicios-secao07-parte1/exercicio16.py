vetor = []

for i in range(5):
    numero = float(input('Informe um número: '))
    vetor.append(numero)

print('\n0 - Finalizar o programa')
print('1 - Imprimir o vetor na ordem direta')
print('2 - Imprimir o vetor na ordem inversa')
codigo = int(input('Informe um código: '))
print()

if codigo == 1:
    print(f'Vetor na ordem direta: {vetor}')
elif codigo == 2:
    print(f'Vetor na ordem inversa: {vetor[::-1]}')
elif codigo != 0 and codigo != 1 and codigo != 2:
    print(f'O código informado é inválido!')
