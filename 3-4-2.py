# coding: utf-8
"""
Обзорно об интернете: http-запросы, html-страницы и requests

Вашей программе на вход подается ссылка на HTML файл.
Вам необходимо скачать этот файл, затем найти в нем все ссылки вида <a ... href="..." ... > и вывести список сайтов, на которые есть ссылка.

https://regexr.com
"""
import requests
import re

url = 'https://pastebin.com/raw/7543p0ns'
#url = input()

#text = requests.get(url).text
text = """
<a href="test#test">
<a title="" href="http://test.com:8080/path/?test#anchor" style="">
<a title= href=http://test.com  class="my list">
<a test="" href=http://test1.com> <a href=http://test2.com><a href=http://test3.com>
<a href=http://test.com>
<A HREF="http://ya.ru">
<a href="//test.com">
<a href =  "//test.com">
<a href=//test.com>
<a title=test download="http://test.com" href="test.com" class="my test" style=>
<a title=test class="my test" href= "test1.com:8080/test/path?get=http://test2.ru/?true" rel="nofollow" style=>
<a  title=test meta="whatever http://test1.com" href =  "test.com?get=http://test2.ru/?true" class="my test" style=  >
<a title="test2.com" href=test1.com?test=https://test3.com class="my list" download="http://test4.com">
<a href="ftp://test.com:22/url?get=true">﻿
"""

pattern = re.compile(r'<a\s*(?:[\w\s\"\=\.\:\/]*)\s*href\s*=\s*(?:\")?(?:https?:|ftp:)?(?:\/\/)?([\w\.\-]+)')
# print(pattern)
urls = pattern.findall(text.lower())
print(urls)
urls_set = set()
for site in urls:
    if not site.startswith(".."):
        urls_set.add(site)

for site in sorted(urls_set):
    print(site)

"""
resp = requests.get(input()).text
sites = set()
for site in re.findall(r'<a.*?href=".*?:\/\/((?:\w|-)+(?:\.(?:\w|-)+)+)', resp):
    sites.add(site)

for site in sorted(sites):
    print(site)
==========================================================

urls = set(re.findall(r"(?:.*)?(?:<a(?:.*)? href=[\"\'])(?:\w+://)?(\w[\w\.-]*)", requests.get(input()).text))

print('\n'.join(sorted(urls)))    
"""