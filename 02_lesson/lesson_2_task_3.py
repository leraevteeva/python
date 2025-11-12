import math


def square(side):
    area = side * side
    return math.ceil(area)


side_length = 4.3
result = square(side_length)
print(f"Площадь квадрата со стороной {side_length}: {result}")
