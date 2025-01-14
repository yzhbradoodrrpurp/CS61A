# -*- coding = utf-8 -*-
# @Time: 2025/1/10 14:14
# @Author: Zhihang Yi
# @File: discussion.py
# @Software: PyCharm

class Link:
    empty = ()

    def __init__(self, first, rest=None):
        self.first = first

        if rest is None:
            self.rest = Link.empty
        else:
            self.rest = rest

def strange_loop():
    """Return a Link s for which s.rest.first.rest is s.

    >>> s = strange_loop()
    >>> s.rest.first.rest is s
    True
    """
    "*** YOUR CODE HERE ***"
    s = Link(Link.empty, Link.empty)
    s.first = s
    s.rest = s
    return s

def sum_rec(s, k):
    """Return the sum of the first k elements in s.

    >>> a = Link(1, Link(6, Link(8)))
    >>> sum_rec(a, 2)
    7
    >>> sum_rec(a, 5)
    15
    >>> sum_rec(Link.empty, 1)
    0
    """
    # Use a recursive call to sum_rec; don't call sum_iter
    "*** YOUR CODE HERE ***"
    if s is not Link.empty:
        if k - 1 != 0:
            return s.first + sum_rec(s.rest, k - 1)
        else:
            return s.first
    else:
        return 0

def sum_iter(s, k):
    """Return the sum of the first k elements in s.

    >>> a = Link(1, Link(6, Link(8)))
    >>> sum_iter(a, 2)
    7
    >>> sum_iter(a, 5)
    15
    >>> sum_iter(Link.empty, 1)
    0
    """
    # Don't call sum_rec or sum_iter
    "*** YOUR CODE HERE ***"
    count = 0
    summary = 0

    while count < k:
        if s is Link.empty:
            break

        summary += s.first
        count += 1
        s = s.rest

    return summary

def overlap(s, t):
    """For increasing s and t, count the numbers that appear in both.

    >>> a = Link(3, Link(4, Link(6, Link(7, Link(9, Link(10))))))
    >>> b = Link(1, Link(3, Link(5, Link(7, Link(8)))))
    >>> overlap(a, b)  # 3 and 7
    2
    >>> overlap(a.rest, b)  # just 7
    1
    >>> overlap(Link(0, a), Link(0, b))
    3
    """
    "*** YOUR CODE HERE ***"
    count = 0

    while True:
        if s is Link.empty or t is Link.empty:
            break

        if s.first == t.first:
            count += 1
            s = s.rest
            t = t.rest
        elif s.first < t.first:
            s = s.rest
        elif s.first > t.first:
            t = t.rest

    return count


