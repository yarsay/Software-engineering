import math

x = lambda: math.cos(5) ** 2
y = lambda z: z ** 3 - 1
func = lambda x, y: x + y

print(func(x(), y(int(input()))))
