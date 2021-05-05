fator1 = 0
fator2 = 0
maior_palindromo = 0

for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        numero = i * j

        if numero > maior_palindromo:
            numero_string = str(numero)
            numero_invertido = numero_string[::-1]

            if numero_string == numero_invertido:
                maior_palindromo = numero
                fator1 = i
                fator2 = j

print(f'Maior palindromo: {fator1} * {fator2} = {maior_palindromo}')
