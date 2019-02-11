# coding: utf-8
"""
Вам дана последовательность строк.
В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
Буквой считается символ из группы \w.
"""

import re
import sys


for line in sys.stdin:
    print(re.sub(r'(\w)\1+', r'\1', line.rstrip()))

"""
[print(re.sub(r'\b(\w)(\w)',r'\2\1', line.strip())) for line in sys.stdin]
"""
