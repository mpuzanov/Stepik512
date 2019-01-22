# coding: utf-8
"""
Вам дана в архиве (ссылка) файловая структура, состоящая из директорий и файлов.
Вам необходимо распаковать этот архив, и затем найти в данной в файловой структуре все директории,
в которых есть хотя бы один файл с расширением ".py".
Ответом на данную задачу будет являться файл со списком таких директорий, отсортированных в лексикографическом порядке.
"""

import os

test_dir = 'C:\\Users\\manager\\Downloads\\main\\'
abc = set()
os.chdir(test_dir)
abc = {current_dir[2:] for current_dir, dirs, files in os.walk(".") for file in files if (file.endswith('.py'))}
[print(s) for s in sorted(abc)]

"""
import os

for cur_dir, subdirs, files in os.walk("main"):
    for file in files:
        if file.endswith(".py"):
            print(cur_dir)
            break
"""