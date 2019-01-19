# -*- coding: utf-8 -*-
'''
Реализуйте класс MoneyBox, для работы с виртуальной копилкой.

Каждая копилка имеет ограниченную вместимость, которая выражается целым числом – количеством монет, 
которые можно положить в копилку. Класс должен поддерживать информацию о количестве монет в копилке, 
предоставлять возможность добавлять монеты в копилку и узнавать, 
можно ли добавить в копилку ещё какое-то количество монет, не превышая ее вместимость.
'''


class MoneyBox:
    def __init__(self, capacity):  # конструктор с аргументом – вместимость копилки              
        self.capacity = capacity
        self.v = 0

    def can_add(self, v):
        # True, если можно добавить v монет, False иначе
        return self.v + v <= self.capacity

    def add(self, v):
        # положить v монет в копилку
        if self.can_add(v):
            self.v += v
    

x = MoneyBox(5)
print(x.v, x.capacity)
print(x.add(3))
print(x.add(2))
print(x.add(3))
