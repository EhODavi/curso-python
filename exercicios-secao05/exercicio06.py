numero1 = int(input('Informe o primeiro número: '))
numero2 = int(input('Informe o segundo número: '))

if numero1 >= numero2:
    print(f'O maior número é o primeiro ({numero1})! A diferença entre eles é {numero1 - numero2}!')
else:
    print(f'O maior número é o segundo ({numero2})! A diferença entre eles é {numero2 - numero1}!')
