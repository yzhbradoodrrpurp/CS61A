# -*- coding = utf-8 -*-
# @Time: 2024/11/16 11:24
# @Author: Zhihang Yi
# @File: 001miscellaneousPython.py
# @Software: PyCharm

# -*- coding = utf-8 -*-
# @Time: 2024/11/5 13:02
# @Author: Zhihang Yi
# @File: 001miscellaneousPython.py
# @Software: PyCharm

"""
在Terminal中输入: 'python 001miscellaneousPython.py' ，会执行这个文件，如果没有Syntax Error就不会有输出。
在Terminal中输入: 'python -i 001miscellaneousPython.py' ，会以交互的方式执行这个文件，你可以在终端中调用这个文件中的某个函数。
在Terminal中输入: 'python -m doctest 001miscellaneousPython.py' ，会执行docstring中的以 '>>>' 开头的Python交互命令。
"""

"""
在Python中，None, 0, '', "" 在进行逻辑判断时，都被视作False，其余的被视为True。
"""

# 在函数的声明中，形式参数变量进行赋值，意味着如果不传入这个参数，那么就默认为赋值的这个数。
def divide_exact(x, y=10):
    """
    This function returns the quotient and remainder of x dividing by y.

    >>> quotient, remainder = divide_exact(15, 3)
    >>> quotient
    5
    >>> remainder
    0

    >>> quotient, remainder = divide_exact(36, 7)
    >>> quotient
    5
    >>> remainder
    1

    >>> quotient, remainder = divide_exact(46, 3)
    >>> quotient
    15
    >>> remainder
    1
    """

    return x // y, x % y
