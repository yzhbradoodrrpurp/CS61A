# -*- coding = utf-8 -*-
# @Time: 2024/11/17 13:22
# @Author: Zhihang Yi
# @File: discussion.py
# @Software: PyCharm


def swipe(n):
    """Print the digits of n, one per line, first backward then forward.

    >>> swipe(2837)
    7
    3
    8
    2
    8
    3
    7
    """
    if n < 10:
        print(n)
    else:
        "*** YOUR CODE HERE ***"
        print(n % 10)
        swipe(n // 10)
        print(n % 10)


def skip_factorial(n):
    """Return the product of positive integers n * (n - 2) * (n - 4) * ...

    >>> skip_factorial(5) # 5 * 3 * 1
    15
    >>> skip_factorial(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 1 or n == 2:
        return n
    else:
        return n * skip_factorial(n - 2)


def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"

    assert n > 1, 'n must be greater than 1.'

    def f(i):
        if n == i:
            return True
        elif n % i == 0:
            return False
        else:
            return f(i + 1)

    return f(2)


def hailstone(n):
    """Print out the hailstone sequence starting at n,
    and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    print(int(n))
    if n % 2 == 0:
        return 1 + even(n)
    else:
        return 1 + odd(n)

def even(n):
    return hailstone(n / 2)

def odd(n):
    """*** YOUR CODE HERE ***"""
    if n != 1:
        return hailstone(3 * n + 1)
    else:
        return 0


def sevens(n, k):
    """Return the (clockwise) position of who says n among k players.

    >>> sevens(2, 5)
    2
    >>> sevens(6, 5)
    1
    >>> sevens(7, 5)
    2
    >>> sevens(8, 5)
    1
    >>> sevens(9, 5)
    5
    >>> sevens(18, 5)
    2
    """

    def f(i, who, direction):
        if i == n:
            return who

        if has_seven(i) or dividable_seven(i):
            direction *= -1

        if direction == 1:
            who += 1
            if who > k:
                who -= k
        elif direction == -1:
            who = who - 1
            if who <= 0:
                who += k

        return f(i + 1, who, direction)

    return f(1, 1, 1)


def has_seven(n):
    if n == 0:
        return False
    elif n % 10 == 7:
        return True
    else:
        return has_seven(n // 10)


def dividable_seven(n):
    return n % 7 == 0

