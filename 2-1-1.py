# coding: utf-8
"""
Вашей программе будет доступна функция foo, которая может бросать исключения.
Вам необходимо написать код, который запускает эту функцию, затем ловит исключения
ArithmeticError, AssertionError, ZeroDivisionError и выводит имя пойманного исключения.
"""


def foo():
    x = 1
    return x / 0


try:
    foo()
except ZeroDivisionError:
    print("ZeroDivisionError")
except ArithmeticError:
    print("ArithmeticError")
except AssertionError:
    print("AssertionError")
