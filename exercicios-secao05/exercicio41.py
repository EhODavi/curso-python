peso = float(input('Informe o peso: '))
altura = float(input('Informe a altura: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('Abaixo do peso')
elif 18.6 <= imc <= 24.9:
    print('Saudável')
elif 25.0 <= imc <= 29.9:
    print('Peso em excesso')
elif 30.0 <= imc <= 34.9:
    print('Obesidade Grau |')
elif 35.0 <= imc <= 39.9:
    print('Obesidade Grau || (severa)')
elif imc >= 40.0:
    print('Obesidade Grau ||| (mórbida)')
