# coding: utf-8
"""
Распространённые форматы текстовых файлов: CSV, JSON

Вам дано описание наследования классов в формате JSON.
Описание представляет из себя массив JSON-объектов, которые соответствуют классам.
У каждого JSON-объекта есть поле name, которое содержит имя класса, и поле parents,
которое содержит список имен прямых предков.
[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в следующем формате.
"""
import json


def f(child, parent):
    if child not in pd2:
        pd2[child] = set()
    for ch in parent:
        if ch not in pd2:
            pd2[ch] = set()
        pd2[child].add(ch)
        f(child, pd[ch])


cld = json.loads(input())
pd = {}
# создадим словарь {Родитель : set(наследники)}
for el_child in cld:
    parent_name = el_child['name']
    list_child = el_child['parents']
    if parent_name not in pd:
        pd[parent_name] = set()
    for el in list_child:
        # print('el', el)
        if el not in pd:
            pd[el] = set()
        pd[el].add(parent_name)

pd2 = {}
for el in pd:
    # print('el', el, pd[el])
    f(el, pd[el])

# print('pd2', pd2)
for key in sorted(pd2):
    print('{} : {}'.format(key, len(pd2[key])+1))

"""
import json

data = json.loads(input())
children = dict()

for cls in data:
    for par in cls["parents"]:
        if par not in children:
            children[par] = []
        children[par].append(cls["name"])

def dfs(v, used):
    size = 1
    used.add(v)
    if v not in children:
        return size

    for child in children[v]:
        if child not in used:
            size += dfs(child, used)

    return size

ans = []

for cls in data:
    ans.append((cls["name"], dfs(cls["name"], set())))

for i in sorted(ans):
    print(i[0], ":", i[1])
    
=========================================================
import json

def test(x, c):
    for i in z:
        if x in i['parents']:
            c.add(i['name'])
            c = test(i['name'], c)
    return (c)

z = json.loads(input())
z.sort(key=(lambda x: x['name']))
for i in z:
    print(i['name'], ':', len(test(i['name'], c = set()))+ 1)
        
"""