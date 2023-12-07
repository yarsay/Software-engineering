import math


def x():
    return math.cos(5) ** 2


def y(z):
    return z ** 3 - 1


def func(x, y):
    return x + y


print(func(x(), y(int(input()))))
