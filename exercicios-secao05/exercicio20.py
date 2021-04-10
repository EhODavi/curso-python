A = float(input('Informe o lado A do triângulo: '))
B = float(input('Informe o lado B do triângulo: '))
C = float(input('Informe o lado C do triângulo: '))

if A < (B + C) and B < (A + C) and C < (A + B):
    if A == B and A == C:
        print('TRIÂNGULO EQUILÁTERO!')
    elif A == B or A == C or B == C:
        print('TRIÂNGULO ISÓSCELES!')
    else:
        print('TRIÂNGULO ESCALENO!')
else:
    print('NÃO É TRIÂNGULO!')
