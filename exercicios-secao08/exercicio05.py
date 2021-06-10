from math import pi


def volume_esfera(raio: float) -> float:
    return (4/3) * pi * (raio ** 3)


print(volume_esfera(5))
print(volume_esfera(10))
print(volume_esfera(7.15))
