# coding: utf-8
"""
Вам дано описание наследования классов в следующем формате. 
<имя класса 1> : <имя класса 2> <имя класса 3> ... <имя класса k>
Это означает, что класс 1 отнаследован от класса 2, класса 3, и т. д.

30 строчек кода: формируем словарь (ключ = предок, значение = список наследников) 
и рекурсивную функцию поиска связи между предком и предполагаемым наследником. 
К слову, у создателя курса Константина Зайцева решение заняло 14 строчек кода !!! 14 !!! 
"""

# import sys
# sys.stdin = open("input_1-6-1.txt", "r")


def is_parent(parent, child):
    # print('is_parent',parent, child)
    if parent == child:
        return True
    if parent in cl and child in cl[parent]:
        return True
    else: 
        res = False
        for i in cl[parent]:
            res = is_parent(i, child)
            if res:
                return res
        return res


cl = {}
n = int(input())

for i in range(n):
    s = input().strip()
    if ':' in s:
        s1, s2 = s.split(':')
        for j in s2.split():
            if j not in cl:
                cl[j] = []
            cl.get(j).append(s1.strip())
        if s1.strip() not in cl:
            cl[s1.strip()] = []
    else:
        if s not in cl:
            cl[s] = []
# print(cl)

q = int(input())
for i in range(q):
    s1, s2 = input().split()
    b = is_parent(s1, s2)
    print('Yes' if b else 'No')
    
"""
Решение преподавателя:

n = int(input())

parents = {}
for _ in range(n):
    a = input().split()
    parents[a[0]] = [] if len(a) == 1 else a[2:]

def is_parent(child, parent):
    return child == parent or any(map(lambda p: is_parent(p, parent), parents[child]))

q = int(input())
for _ in range(q):
    a, b = input().split()
    print("Yes" if is_parent(b, a) else "No")
"""
