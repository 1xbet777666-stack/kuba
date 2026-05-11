import math

x1 = float(input("Введите х1: "))
xn = float(input("Введите хn: "))
dx = float(input("Введите dx: "))
a = 3.9

if dx <= 0:
    raise ValueError("dx должен быть больше 0")

while x1 < xn:
    y = math.sin(1 / math.sqrt(a * x1 ** 2 + 2) + math.exp(x1))
    print("при х = ", x1, "y = ", "{0:.4f}".format(y))
    x1 = x1 + dx