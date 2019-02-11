# coding: utf-8
"""
В этой задаче вам необходимо воспользоваться API сайта artsy.net
API проекта Artsy предоставляет информацию о некоторых деятелях искусства, их работах, выставках.

Вам даны идентификаторы художников в базе Artsy.
Для каждого идентификатора получите информацию о имени художника и годе рождения.
Выведите имена художников в порядке неубывания года рождения. В случае если у художников одинаковый год рождения,
выведите их имена в лексикографическом порядке.

Client Id	08c8433a09a9a0e70cc5
Client Secret	45cefcfef9434d89f3cbe17eafa70c15
"""

import requests
import json

client_id = '08c8433a09a9a0e70cc5'
client_secret = '45cefcfef9434d89f3cbe17eafa70c15'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token": token}

def getArtists(id):
    # инициируем запрос с заголовком
    r = requests.get("https://api.artsy.net/api/artists/"+id, headers=headers)
    # r.encoding = 'utf-8'
    # text = r.text
    #text =
    # разбираем ответ сервера
    j = json.loads(r.content.decode('utf-8'))
    return (j['sortable_name'], int(j['birthday']), id)

# id = '4f86f41a24907b0001000d46'  https://api.artsy.net/api/artists/4f86f41a24907b0001000d46
# print(getArtists(id))

artists = []
with open('dataset_24476_4.txt', 'r', encoding="utf-8") as fr:
     for id in fr:
        artists.append(getArtists(id.rstrip()))

with open('final.txt', 'wt', encoding='utf-8') as file:  #
    for art in sorted(artists, key=lambda x: (x[1], x[0])):
        file.write(art[0]+'\n')
        print(art[0])  # , art[1], art[2])

"""
import requests
import json

# put your id and secret here
client_id = '...'
client_secret = '...'

resp = requests.post("https://api.artsy.net/api/tokens/xapp_token";, data={"client_id" : client_id, "client_secret" : client_secret}).text
token = json.loads(resp)["token"]

def get_json(url):
    headers = {"X-Xapp-Token" : token}
    resp = requests.get(url, headers=headers).text
    return json.loads(resp)

ans = []

with open("input.txt") as inp:
    for id in inp:
        id = id.rstrip()
        js = get_json("https://api.artsy.net/api/artists/"; + id)
        ans.append((js["birthday"], js["sortable_name"]))

ans.sort(key=lambda x: (int(x[0]), x[1]))
﻿
print("\n".join(map(lambda x: x[1], ans)))
===============================================

res = []
with open('dataset_24476_4.txt', 'r') as f, open('result.txt', 'w', encoding='utf-8') as w:
    for i in f:
        req_str = 'https://api.artsy.net/api/artists/' + i.rstrip()
        j = requests.get(req_str, headers=headers).json() 
        res.append(j['birthday']+j['sortable_name'])
    for i in sorted(res):
        w.write(i[4:]+'\n')﻿
        
"""