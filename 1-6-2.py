# coding: utf-8
'''
Реализуйте структуру данных, представляющую собой расширенную структуру стек. 
Необходимо поддерживать добавление элемента на вершину стека, удаление с вершины стека, 
и необходимо поддерживать операции сложения, вычитания, умножения и целочисленного деления
'''
class ExtendedStack(list):
    def sum(self):
        # операция сложения
        self.append(self.pop()+self.pop())

    def sub(self):
        # операция вычитания
        self.append(self.pop()-self.pop())

    def mul(self):
        # операция умножения
        self.append(self.pop()*self.pop())

    def div(self):
        # операция целочисленного деления
        self.append(self.pop()//self.pop())

def test():
    ex_stack = ExtendedStack([1, 2, 3, 4, -3, 3, 5, 10])
    ex_stack.div()
    assert ex_stack.pop() == 2
    ex_stack.sub()
    assert ex_stack.pop() == 6
    ex_stack.sum()
    assert ex_stack.pop() == 7
    ex_stack.mul()
    assert ex_stack.pop() == 2
    assert len(ex_stack) == 0

test()        