# coding: utf-8
"""
Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве слова.

Примечание:
Для работы со словами используйте группы символов \b и \B.
"""

import re
import sys

patern = r'\bcat\b'

for line in sys.stdin:
    line = line.rstrip()
    result = re.findall(patern, line)
    if len(result) > 0:
        print(line)

"""
for line in sys.stdin:
    line = line.rstrip()
    if re.search(r"\bcat\b", line):
        print(line)
"""


