# coding: utf-8
"""
Вам дана последовательность строк.
В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
Буквой считается символ из группы \w.
"""

import sys

pattern = r'[10]+'

for line in sys.stdin:
    line = line.rstrip()
    try:
        num = int(line, base=2)
        if num % 3 == 0:
            print(line)
    except Exception:
        continue

"""
import re
import sys

pattern = "^(0|(1(01*0)*1))*$"
pattern = re.compile(pattern)
for line in sys.stdin:
    line = line.rstrip()
    if pattern.match(line):
        print(line)
        
        
import sys, re
sys.stdout.writelines(filter(re.compile(r"^(1(01*0)*1|0)+$").match, sys.stdin))        
"""
