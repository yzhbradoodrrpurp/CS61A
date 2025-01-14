# -*- coding = utf-8 -*-
# @Time: 2024/11/16 11:23
# @Author: Zhihang Yi
# @File: 002HigherOrderFunction.py
# @Software: PyCharm

# -*- coding = utf-8 -*-
# @Time: 2024/11/13 18:54
# @Author: Zhihang Yi
# @File: HigherOrderFunction.py
# @Software: PyCharm

"""
高阶函数(Higher-Order Function)是一种能够接收其它函数为变量，或者返回一个函数变量的函数。
下面的例子中，summation()是接收一个函数作为变量，make_adder()是返回一个函数变量。
"""

from math import sqrt, pi


def summation(n, function):
    """
    >>> summation(5, cube)
    225
    >>> summation(100, natural)
    5050
    >>> summation(100, pi_term)
    3.1365926848388144

    :param n: a natural number.
    :param function: a function to call
    :return: a natual number calculated based on the function called.
    """
    assert n > 0, 'The variable must be positive.'

    summary = 0

    for i in range(1, n + 1):
        summary += function(i)

    return summary


def cube(n):
    return n ** 3

def natural(n):
    return n

def pi_term(n):
    return 8 / ((4 * n - 3) * (4 * n - 1))


def make_adder(n):
    """
    >>> make_adder(5)(3)
    8
    >>> make_adder(1000)(5)
    1005
    >>> make_adder(0)(1)
    1
    >>> adder = make_adder(10)
    >>> adder(8)
    18
    >>> adder = make_adder(4)
    >>> adder(0)
    4

    :param n: the added number
    :return: a total of n and k(passed to the nested function.)
    """
    def adder(k):
        return n + k

    return adder


