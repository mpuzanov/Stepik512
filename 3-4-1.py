# coding: utf-8
"""
Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.
"""
import requests
from re import findall

result = 'No'
url = input()  # 'https://stepic.org/media/attachments/lesson/24472/sample0.html'
url_find = input()  # 'https://stepic.org/media/attachments/lesson/24472/sample2.html'
res = requests.get(url)
#print(res.status_code)
#print(res.headers["Content-Type"])
#print(res.text)
patern = r'(https?://[^\s]+)"'
urls = findall(patern, res.text)
for url in urls:
    print(url)
    res = requests.get(url)
    urls2 = findall(patern, res.text)
    for url2 in urls2:
        if url2 == url_find:
            result = 'Yes'

print(result)

"""
start_url = input()
end_url = input()

found = False

link_pattern = re.compile(r'<a[^>]*?href="(.*?)"[^>]*?>')

resp = requests.get(start_url).text
for url in link_pattern.findall(resp):
    cur_resp = requests.get(url).text
    if end_url in link_pattern.findall(cur_resp):
        found = True
        break

print("Yes" if found else "No")

=========================================
import requests, re

urls = [input() for cmd in range(2)]
p = 'No'

for i in re.findall(r'<a.*href="(.*)">', requests.get(urls[0]).text):
    if urls[1] in re.findall(r'<a.*href="(.*)">', requests.get(i).text):
        p = 'Yes'
        break

print(p)
==========================================
import requests, re
A, B, T = input(), input(), re.compile(r'<a\s+href\s*=\s*"(.+)"')
print("Yes" if B in (D for C in T.findall(requests.get(A).text) for D in T.findall(requests.get(C).text)) else "No")

"""