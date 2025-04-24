import math

def square(a):
    square = a * a
    return math.ceil (square)

a = float(input("введите сторону квадрата:"))
area = square(a)

print(f"площадь квадрата={area}")