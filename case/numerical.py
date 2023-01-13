import sympy as sy
import matplotlib.pyplot as plt
import numpy as np
import time
import math

from interpolation3 import lagrange_interpolation, lagrange_interpolation_
from numerical_integral5 import NewtonCotes1, NewtonCotes2, GaussianQuadrature

from systems_of_equations2 import Sor
from systems_of_equations2 import gauss_seidel

x = sy.symbols('x')


"""做一个《有限元法上》p430的例子。"""
def fem_case1():
    a = [0, 1, 3]
    b = [1, 1, 5]
    p = lagrange_interpolation(a, b)
    print(p)

"""做一个《有限元法上》p431的例子。"""
def fem_case2():
    f = 2 ** x - x
    array = [0, 3]
    newtoncotes2 = NewtonCotes2(f, array)
    value = newtoncotes2.cal()
    error = newtoncotes2.cal_error(8*math.log(2)**4)
    print('value=%.6f, error=%.6f' % (value, error))

def fem_case3():
    f = 2 ** x - x
    array = [0, 3]
    newtoncotes2 = NewtonCotes2(f, array)
    value = newtoncotes2.cal(2)
    error = newtoncotes2.cal_error(8 * math.log(2) ** 4)
    print('value=%.6f, error=%.6f' % (value, error))

def fem_case4():
    f = [x ** 3 + 3, 10 + (x - 1) ** (1 / 3), (13 - x) ** 5 / 128 + 4]
    array = [-1, 2, 9, 13]
    array0 = [[-1, 2], [2, 9], [9, 13]]
    f_c = [0, 80/81, 3.75]
    value = 0
    error = 0
    for i in range(len(f)):
        newtoncotes2 = NewtonCotes2(f[i], array0[i])
        value += newtoncotes2.cal()
        error += newtoncotes2.cal_error(f_c[i])
    print('value=%.6f, error=%.6f' % (value, error))

def case0():
    f = 2 ** x -x
    gaussian = GaussianQuadrature(f, [0, 3])
    value = gaussian.cal(2)
    print('value=%.8f' % value)

case0()

