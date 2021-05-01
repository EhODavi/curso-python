N = int(input('Informe um número: '))

print(f'Os {N} primeiros números ímpares são: ')
contador = 1
for i in range(N):
    print(contador)
    contador = contador + 2
