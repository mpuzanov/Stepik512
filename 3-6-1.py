# coding: utf-8
"""
API

В этой задаче вам необходимо воспользоваться API сайта numbersapi.com

Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует ли интересный математический факт об этом числе.

Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе.
Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.
"""
import requests


def fun(number):
    api_url = "http://numbersapi.com/{}/math".format(number)  # http://numbersapi.com/31/math?json=true
    params = {
        'json': True
    }
    res = requests.get(api_url, params=params)
    # print(res.url)
    # print(res.status_code)
    # print(res.headers['Content-Type'])
    data = res.json()
    # print(data)
    result = 'Boring'
    if data['found']:
        result = 'Interesting'
    return result


# num = 99
with open("dataset_24476_3.txt", "r") as f:
    for s in f:
        # print(s)
        print(fun(int(s.rstrip())))

"""
import requests
import json

def is_interesting(x):
    url = "http://numbersapi.com/"; + str(x) + "/math?json=true"
    resp = requests.get(url).text
    js = json.loads(resp)
    return js["found"]

with open("input.txt") as fi:
    for line in fi:
        print("Interesting" if is_interesting(line.rstrip()) else "Boring")
===================================================================
import requests as re

with open('dataset_24476_3.txt') as file:
    for num in file:
        response = re.get('http://numbersapi.com/{number}/math?json=true'.format( number=num.rstrip() )).json()﻿
        ﻿
        print('Interesting') if response['found'] else print('Boring')﻿        
"""