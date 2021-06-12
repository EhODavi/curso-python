def ler():
    p = input('Informe a fração p: ')
    q = input('Informe a fração q: ')

    p = p.split('/')
    q = q.split('/')

    p = [int(p[0]), int(p[1])]
    q = [int(q[0]), int(q[1])]

    p = simplifica(p)
    q = simplifica(q)

    operacoes(p, q)


def simplifica(fracao):
    menor = min(fracao[0], fracao[1])

    for divisor in range(menor, 1, -1):
        if fracao[0] % divisor == 0 and fracao[1] % divisor == 0:
            fracao[0] /= divisor
            fracao[1] /= divisor

    return [int(fracao[0]), int(fracao[1])]


def operacoes(p, q):
    print('\nResultados:\n')

    r = soma(p, q)
    print(f'{p[0]}/{p[1]} + {q[0]}/{q[1]} = {int(r[0])}/{int(r[1])}')

    r = subtracao(p, q)
    print(f'{p[0]}/{p[1]} - {q[0]}/{q[1]} = {int(r[0])}/{int(r[1])}')

    r = multiplicacao(p, q)
    print(f'{p[0]}/{p[1]} * {q[0]}/{q[1]} = {int(r[0])}/{int(r[1])}')

    r = divisao(p, q)
    print(f'{p[0]}/{p[1]} / {q[0]}/{q[1]} = {int(r[0])}/{int(r[1])}')


def soma(p, q):
    r = [p[0] * q[1] + q[0] * p[1], p[1] * q[1]]

    r = simplifica(r)

    return r


def subtracao(p, q):
    r = [p[0] * q[1] - q[0] * p[1], p[1] * q[1]]

    r = simplifica(r)

    return r


def multiplicacao(p, q):
    r = [p[0] * q[0], p[1] * q[1]]

    r = simplifica(r)

    return r


def divisao(p, q):
    r = [p[0] * q[1], p[1] * q[0]]

    r = simplifica(r)

    return r


ler()
