encontrei = False

for a in range(1001):
    if encontrei:
        break
    for b in range(1001):
        if encontrei:
            break
        for c in range(1001):
            if encontrei:
                break
            if a ** 2 + b ** 2 == c ** 2 and a + b + c == 1000:
                print(f'a = {a}')
                print(f'b = {b}')
                print(f'c = {c}')

                encontrei = True
