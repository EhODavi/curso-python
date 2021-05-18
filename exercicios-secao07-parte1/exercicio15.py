vetor = []
vetor_sem_repetidos = []

for i in range(20):
    numero = int(input('Informe um número: '))
    vetor.append(numero)

for i in range(20):
    if vetor.count(vetor[i]) == 1:
        vetor_sem_repetidos.append(vetor[i])

print(f'Vetor: {vetor}')
print(f'Vetor sem repetição: {vetor_sem_repetidos}')
