# coding: utf-8
"""
Вам дана последовательность строк.
Выведите строки, содержащие две буквы "z﻿", между которыми ровно три символа
"""

import re
import sys

patern = r'z\w\w\wz'

for line in sys.stdin:
    line = line.rstrip()
    if re.search(patern, line):
        print(line)

