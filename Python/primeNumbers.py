"""Implementation of Basic Math in Python."""
import math


def prime_factors(n: int) -> list:
    """Find Prime Factors.
    >>> prime_factors(100)
    [2, 2, 5, 5]
    """
    pf = []
    while n % 2 == 0:
        pf.append(2)
        n = int(n / 2)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            pf.append(i)
            n = int(n / i)
    if n > 2:
        pf.append(n)
    return pf
