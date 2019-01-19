# coding: utf-8
"""
Вам дано описание наследования классов исключений в следующем формате.
<имя исключения 1> : <имя исключения 2> <имя исключения 3> ... <имя исключения k>
Это означает, что исключение 1 наследуется от исключения 2, исключения 3, и т. д.

Или эквивалентно записи:
class Error1(Error2, Error3 ... ErrorK):
    pass
Антон написал код, который выглядит следующим образом.

try:
   foo()
except <имя 1>:
   print("<имя 1>")
except <имя 2>:
   print("<имя 2>")
...
Костя посмотрел на этот код и указал Антону на то, что некоторые исключения можно не ловить,
так как ранее в коде будет пойман их предок. Но Антон не помнит какие исключения наследуются от каких.
Помогите ему выйти из неловкого положения и напишите программу,
которая будет определять обработку каких исключений можно удалить из кода.

"""


def is_parent(child, parent):
    if child in out:
        return True
    else:
        # if len(parent) == 0:
        out.add(child)
        for _ in parent:
            is_parent(_, cl[_])


cl = {}
out = set()
err = []
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
    s = input().strip()
    # print(s)
    if is_parent(s, cl[s]):
        err.append(s)
    else:
        out.add(s)

# print(out)
for _ in err:
    print(_)

"""
n = int(input())
classes = {}
for i in range(n):
    line = input()
    parts = line.split(" : ")
    cls = parts[0]
    if len(parts) == 1:
        classes[cls] = []
    else:
        classes[cls] = parts[1].split(" ")


def check(src, dest):
    if src == dest:
        return True
    return any([check(child, dest) for child in classes[src]])


m = int(input())
used = []

for i in range(m):
    cls = input()
    if any([check(cls, used_one) for used_one in used]):
        print(cls)
    used.append(cls)
"""