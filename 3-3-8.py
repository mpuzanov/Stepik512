# coding: utf-8
"""
Вам дана последовательность строк.
В каждой строке поменяйте местами две первых буквы в каждом слове, состоящем хотя бы из двух букв.
Буквой считается символ из группы \w
"""

import re
import sys

# text = "We arrive on 03/25/2018. So you are welcome after 04/01/2018."
# print(re.sub(r'(\d\d)/(\d\d)/(\d{4})', r'\2.\1.\3', text))
# # -> We arrive on 25.03.2018. So you are welcome after 01.04.2018.

for line in sys.stdin:
    print(re.sub(r'\b(\w)(\w)(\w*)\b', r'\2\1\3', line.rstrip()))

"""
[print(re.sub(r'\b(\w)(\w)',r'\2\1', line.strip())) for line in sys.stdin]
"""
