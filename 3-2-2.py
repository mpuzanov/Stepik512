# coding: utf-8
"""
Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.

Выведите одно число – количество вхождений строки t в строку s.
"""

s, t = input(), input()
start, kol = 0, 0
while start < len(s):
    start = s.find(t, start)
    # print(start)
    if start > -1:
        kol += 1
    else:
        break
    start += 1
print(kol)

"""
s = input()
t = input()
ans = 0
for i in range(len(s)):
    if s[i:].startswith(t):
        ans += 1
print(ans)

#  2 вариант
s = input()
t = input()
print(sum(1 for i in range(len(s)) if s.startswith(t, i)))

"""