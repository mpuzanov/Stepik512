# coding: utf-8
'''
Вам дано описание наследования классов в следующем формате. 
<имя класса 1> : <имя класса 2> <имя класса 3> ... <имя класса k>
Это означает, что класс 1 отнаследован от класса 2, класса 3, и т. д.

30 строчек кода: формируем словарь (ключ = предок, значение = список наследников) 
и рекурсивную функцию поиска связи между предком и предполагаемым наследником. 
К слову, у создателя курса Константина Зайцева решение заняло 14 строчек кода !!! 14 !!! 

'''

# import sys
# sys.stdin = open("input_1-6-1.txt", "r")

n = int(input())
cl = {}
for i in range(n):
    s = input()
    if ':' in s:
        s1, s2 = s.split(':')
        cl[s1.strip()] = s2.split()
    else:
        cl[s] = []
print(cl)
q = int(input())
for i in range(q):
    b = False
    s1, s2 = input().split()
    if s1 in cl[s2] or s1 == s2:
        b = True
    else:
        if s2 in cl:
            # print(s2,'есть в cl')
            for j in range(len(cl[s2])):
                k = cl[s2][j]
                # print(k)
                if k in cl and s1 in cl[k]:
                    b = True

    print('Yes' if b else 'No')
