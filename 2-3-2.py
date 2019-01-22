# coding: utf-8
"""
Реализуйте функцию-генератор primes, которая будет генерировать простые числа в порядке возрастания, начиная с числа 2.
"""

import itertools
import math


def primes():
    a = 1
    while True:
        a += 1
        # проверить что число простое (теорема Вильсена)
        if ((math.factorial(a - 1) + 1) % a) == 0:
            yield a


print(list(itertools.takewhile(lambda x: x <= 31, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

"""
def primes():
    c, f = 2, 1
    while 1:
        if not (f + 1) % c: yield c
        f, c = f * c, c + 1
"""
