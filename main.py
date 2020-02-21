#!/usr/bin/env python
"""Implements math functions without using operators except for '+' and '-' """

__author__ = "dbmiddle"


def add(x, y):
    """Add two integers. Handles negative values."""
    return x + y


def multiply(x, y):
    """Multiply x with y. Handles negative values of x or y."""
    count = 0
    if x < 0:
        return -multiply(-x, y)
    for i in range(x):
        count += add(0, y)
    return count


def power(x, n):
    """Raise x to power n, where n >= 0"""
    count = x
    for i in range(1, n):
        count = multiply(count, x)
    return count


def factorial(x):
    """Compute factorial of x, where x > 0"""
    if x == 0 or x == 1:
        return 1
    for i in range(x-1, 0, -1):
        x = multiply(x, i)
    return x


def fibonacci(n):
    """Compute the nth term of fibonacci sequence"""
    x = [0, 1]
    for i in range(2, n+1):
        x.append(x[i - 2] + x[i - 1])
    return x[n - 1]


if __name__ == '__main__':
    print(add(3, 2))
    print(multiply(5, 4))
    print(power(2, 3))
    print(factorial(5))
    print(fibonacci(8))

