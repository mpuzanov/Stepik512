# coding: utf-8
"""
Работа с файловой системой и файлами

Вам дается текстовый файл, содержащий некоторое количество непустых строк.
На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.
"""

# with open('module2\\tests\\test.txt', 'r') as fr, open('module2\\\\tests\\test_revers.txt', 'w') as fw:
with open('dataset_24465_4.txt', 'r') as fr, open('dataset_24465_revers.txt', 'w') as fw:
    lines = [s.rstrip() for s in fr.readlines()]
    for s in reversed(lines):
        fw.write(s+'\n')


"""
with open('dataset_24465_4.txt', 'r') as fr, open('dataset_24465_4_w.txt', 'w') as fw:
    fw.writelines(fr.readlines()[::-1])
    
    
with open('1.txt') as f, open('2.txt','w') as w:
    w.write('\n'.join(f.read().splitlines()[::-1]))
        
"""