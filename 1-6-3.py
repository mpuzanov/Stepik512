# coding: utf-8
'''
Реализуйте класс LoggableList, отнаследовав его от классов list и Loggable таким образом, 
чтобы при добавлении элемента в список посредством метода append в лог отправлялось сообщение, 
состоящее из только что добавленного элемента.
'''
import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    def append(self, a):
        super(LoggableList, self).append(a)
        self.log(a)


test = LoggableList()
test.append(2)
test.append(4)
print(test)

'''
class LoggableList(list, Loggable):
    def append(self, x):
        list.append(self, x)
        self.log(x)
'''
