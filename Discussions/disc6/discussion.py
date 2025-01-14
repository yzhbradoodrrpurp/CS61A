# -*- coding = utf-8 -*-
# @Time: 2024/12/3 15:15
# @Author: Zhihang Yi
# @File: discussion.py
# @Software: PyCharm

def gen_fib():
    """
    >>> next(filter(lambda x: x > 2024, gen_fib()))
    2584
    """
    n, add = 0, 1
    while True:
        yield n
        n, add = n + add, n


def differences(t):
    """Yield the differences between adjacent values from iterator t.

    >>> list(differences(iter([5, 2, -100, 103])))
    [-3, -102, 203]
    >>> next(differences(iter([39, 100])))
    61
    """
    "*** YOUR CODE HERE ***"
    t = list(t)

    for i in range(len(t) - 1):
        yield t[i + 1] - t[i]


def partition_gen(n, m):
    """Yield the partitions of n using parts up to size m.

    >>> for partition in sorted(partition_gen(6, 4)):
    ...     print(partition)
    1 + 1 + 1 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 2
    1 + 1 + 1 + 3
    1 + 1 + 2 + 2
    1 + 1 + 4
    1 + 2 + 3
    2 + 2 + 2
    2 + 4
    3 + 3
    """
    assert n > 0 and m > 0
    if n == m:
        yield str(n)
    if n - m > 0:
        "*** YOUR CODE HERE ***"
        for p in partition_gen(n - m, min(n - m, m)):
            yield p + ' + ' + str(m)
    if m > 1:
        "*** YOUR CODE HERE ***"
        yield from partition_gen(n, m - 1)

