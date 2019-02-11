# coding: utf-8
"""
XML, библиотека ElementTree, библиотека lxml

Вам дано описание пирамиды из кубиков в формате XML.
Кубики могут быть трех цветов: красный (red), зеленый (green) и синий (blue﻿).
Для каждого кубика известны его цвет, и известны кубики, расположенные прямо под ним.

Введем понятие ценности для кубиков. Самый верхний кубик, соответствующий корню XML документа имеет ценность 1.
Кубики, расположенные прямо под ним, имеют ценность 2.
Кубики, расположенные прямо под нижележащими кубиками, имеют ценность 3. И т. д.
Ценность цвета равна сумме ценностей всех кубиков этого цвета.

Выведите через пробел три числа: ценности красного, зеленого и синего цветов.
"""
from xml.etree import ElementTree


def get_children(current_root, level):
    level += 1
    res[current_root.attrib['color']] += level
    for child_root in current_root:
        get_children(child_root, level)


res = {'red': 0, 'green': 0, 'blue': 0}
str_xml = input()

tree = ElementTree.ElementTree(ElementTree.fromstring(str_xml))
root = tree.getroot()

get_children(root, 0)

print('{} {} {}'.format(res['red'], res['green'], res['blue']))

"""
https://stackoverflow.com/questions/17275524/xml-etree-elementtree-get-node-depth

from xml.etree import ElementTree

root = ElementTree.fromstring(input())
colors = {"red": 0, "green": 0, "blue": 0}

def getcubes(root, value):
    colors[root.attrib['color']] += value
    for child in root:
        getcubes(child, value+1)

getcubes(root,1)
print(colors["red"], colors["green"], colors["blue"])

==============================================================
from xml.etree import ElementTree
colors = {"red": 0, "green": 0, "blue": 0}  # словарь ключ=цвет
def finder(root, count=1):
    colors[root.attrib["color"]] += count  # нашли цвет добавили к счётчику
    [finder(child, count + 1) for child in root]  # поиск во вложениях        
finder(ElementTree.fromstring(input()))  # считываем xml-строку
print(colors["red"], colors["green"], colors["blue"])  # выдаём ответ

"""