contador = 1

while True:
    divisivel_todos = True

    for i in range(1, 21):
        if not contador % i == 0:
            divisivel_todos = False
            break

    if divisivel_todos:
        print(contador)
        break

    contador = contador + 1
