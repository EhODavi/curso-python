print('Usando o for:')

for i in range(1, 101):
    print(i)

print('Usando o while:')

contador = 1

while contador <= 100:
    print(contador)
    contador = contador + 1

print('Usando o do while:')

contador = 1

while True:
    if contador == 101:
        break
    print(contador)
    contador = contador + 1
