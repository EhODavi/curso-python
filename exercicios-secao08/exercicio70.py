def reduz(a, b):
    return a, b


def neg(x):
    return -x[0], x[1]


def soma(x, y):
    return x[0] * y[1] + y[0] * x[1], x[1] * y[1]


def mult(x, y):
    return x[0] * y[0], x[1] * y[1]


def div(x, y):
    return x[0] * y[1], x[1] * y[0]
