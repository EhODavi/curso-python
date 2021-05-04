numero_usuario = int(input('Informe um número positivo: '))

numero1 = 0
numero2 = 1

print(numero1)
print(numero2)

while True:
    numero3 = numero1 + numero2

    print(numero3)

    if numero3 > numero_usuario:
        break

    numero1 = numero2
    numero2 = numero3
