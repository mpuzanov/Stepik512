# coding: utf-8
"""
Реализуйте класс PositiveList, отнаследовав его от класса list, для хранения положительных целых чисел.
Также реализуйте новое исключение NonPositiveError.

В классе PositiveList переопределите метод append(self, x) таким образом, чтобы при попытке добавить неположительное
целое число бросалось исключение NonPositiveError и число не добавлялось,
а при попытке добавить положительное целое число, число добавлялось бы как в стандартный list.

В данной задаче гарантируется, что в качестве аргумента x метода append всегда будет передаваться целое число.

Примечание:
Положительными считаются числа, строго большие нуля.
"""


class NonPositiveError(Exception):
    pass


class PositiveList(list):

    def append(self, x):
        if x <= 0:
            raise NonPositiveError('NonPositiveError')
        else:
            super(PositiveList, self).append(x)  # аналог list.append(self)


# тестируем
a = PositiveList()
a.append(3)
print(a)
a.append(-1)
print(a)

"""
class NonPositiveError(ArithmeticError):
    pass

class PositiveList(list):
    def append(self, x):
        if x <= 0:
            raise NonPositiveError
        super().append(x)
"""
