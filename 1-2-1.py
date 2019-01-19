# -*- coding: utf-8 -*-
'''
Реализуйте программу, которая будет вычислять количество различных объектов в списке.
'''
objects=[1,2,3,4,1,2,3,4,5,6,1,1,1]

n = len(objects)
ans = n
for i in range(n):
    for j in range(i):
        if id(objects[i]) == id(objects[j]):
            ans -= 1
            break

print(ans)

'''
print(len(set(id(i) for i in objects)))
или
print(len({id(x) for x in objects}))
или
s=set()
for obj in objects:
    s.add(id(obj))
print(len(s))

'''