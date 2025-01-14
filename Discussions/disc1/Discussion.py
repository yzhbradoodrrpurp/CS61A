# -*- coding = utf-8 -*-
# @Time: 2024/11/5 15:25
# @Author: Zhihang Yi
# @File: Discussion.py
# @Software: PyCharm


def race(x, y):
    """The tortoise always walks x feet per minute, while the hare repeatedly
    runs y feet per minute for 5 minutes, then rests for 5 minutes. Return how
    many minutes pass until the tortoise first catches up to the hare.
    >>> race(5, 7) # After 7 minutes, both have gone 35 steps
    7
    >>> race(2, 4) # After 10 minutes, both have gone 20 steps
    10
    """
    assert y > x and y <= 2 * x, 'the hare must be fast but not too fast'
    tortoise, hare, minutes = 0, 0, 0

    while minutes == 0 or tortoise - hare:
        tortoise += x
        if minutes % 10 < 5:
            hare += y
        minutes += 1

    return minutes


def fizzbuzz(n):
    """
    This function takes in an integer N and generates a series of numbers ranging from 1 to N.
    The function prints 'fizzbuzz' if it is dividable by both 3 and 5,
    prints 'fizz' if it is only dividable by 3,
    prints 'buzz' if it is only dividable by 5
    and prints the number itself if it is not dividable by neither 3 and 5.

    >>> fizzbuzz(15)
    1 2 fizz 4 buzz fizz 7 8 fizz buzz 11 fizz 13 14 fizzbuzz
    >>> fizzbuzz(3)
    1 2 fizz
    >>> fizzbuzz(5)
    1 2 fizz 4 buzz
    """

    for i in range(1, n + 1):
        if i != n:
            if i % 3 == 0 and i % 5 == 0:
                print('fizzbuzz', end=' ')
            elif i % 3 == 0:
                print('fizz', end=' ')
            elif i % 5 == 0:
                print('buzz', end=' ')
            else:
                print(i, end=' ')
        else:
            if i % 3 == 0 and i % 5 == 0:
                print('fizzbuzz')
            elif i % 3 == 0:
                print('fizz')
            elif i % 5 == 0:
                print('buzz')
            else:
                print(i)


def is_prime(n):
    """
    This function checks if N is a prime number.

    >>> is_prime(4)
    False
    >>> is_prime(5)
    True
    >>> is_prime(1)
    False
    """

    if n == 1:
        return False
    else:
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                return False

        return True


def unique_digits(n):
    """
    :param n: n, an integer, is passed into the function.
    :return: The function returns a list of all the unique digits that belong to n.

    >>> unique_digits(1231231234)
    [1, 2, 3, 4]
    >>> unique_digits(43542)
    [2, 3, 4, 5]
    """

    n = str(n)
    unique_digit_list = []

    for i in n:
        unique_digit_list.append(int(i))

    unique_digit_list = set(unique_digit_list)
    unique_digit_list = list(unique_digit_list)

    return unique_digit_list
