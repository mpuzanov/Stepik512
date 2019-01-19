# -*- coding: utf-8 -*-
"""
Вам дается последовательность целых чисел и вам нужно ее обработать и вывести на экран 
сумму первой пятерки чисел из этой последовательности, затем сумму второй пятерки, и т. д
"""


class Buffer:
    def __init__(self):
        self.lst = []

    def add(self, *a):
        # добавить следующую часть последовательности
        self.lst.extend(a)
        while len(self.lst) >= 5:
            print(sum(self.lst[0:5]))
            del self.lst[0:5]
        return self.lst
    
    def get_current_part(self):
        return self.lst


buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part()  # вернуть [1, 2, 3]
buf.add(4, 5, 6)  # print(15) – вывод суммы первой пятерки элементов
buf.get_current_part()  # вернуть [6]
buf.add(7, 8, 9, 10)  # print(40) – вывод суммы второй пятерки элементов
buf.get_current_part()  # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)  # print(5), print(5) – вывод сумм третьей и четвертой пятерки
buf.get_current_part()  # вернуть [1]

'''
class Buffer:
    def __init__(self):
        self.part = []

    def add(self, *a):
        for i in a:
            self.part.append(i)
            if len(self.part) == 5:
                print(sum(self.part))
                self.part.clear()

    def get_current_part(self):
        return self.part
'''        