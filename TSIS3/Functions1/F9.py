import math


def volume(radius):
    volume = 4 / 3 * math.pi * (radius ** 3)
    return volume


radius = float(input())
print(volume(radius))