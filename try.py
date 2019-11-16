from sympy import *
x = Symbol('x')
y = Symbol('y')
print solve([2 * x - y - 3, 3 * x + y - 7],[x, y])