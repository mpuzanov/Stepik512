# coding: utf-8
"""
Вам дана последовательность строк.
В каждой строке замените первое вхождение слова, состоящего только из латинских букв "a"
(регистр не важен), на слово "argh".
"""

import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(r'\b[a]+\b', r'argh', line, 1, re.IGNORECASE))

"""
sys.stdout.writelines(map(lambda x: re.sub(r"\ba+\b","argh", x, count=1, flags = re.IGNORECASE), sys.stdin))
"""
