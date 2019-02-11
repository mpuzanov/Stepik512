# coding: utf-8
"""
Вам дана последовательность строк.
В каждой строке замените все вхождения подстроки "human" на подстроку "computer"﻿ и выведите полученные строки.
"""

import re
import sys

for line in sys.stdin:
    print(re.sub(r'human', r'computer', line.rstrip()))

"""
print(re.sub(r'human', 'computer', sys.stdin.read()), end='')

"""