# coding: utf-8

"""
Регулярные выражения в Python
Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.
"""

import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    result = re.findall(r'cat', line)
    if len(result) > 1:
        print(line)

"""
import re
import sys

for line in sys.stdin:
    line = line.strip()
    if re.search(r"cat.*cat", line):
        print(line)
        
        
import sys
print(*(s for s in sys.stdin if s.count('cat') > 1), sep='')
        
"""
