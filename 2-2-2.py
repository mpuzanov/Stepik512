# coding: utf-8
"""
Расшифровываем текст из файла - подбираем пароль из файла
"""
import simplecrypt

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()

with open("passwords.txt", "rb") as fpsw:
    passwords = fpsw.read().splitlines()

for s in passwords:
    psw = s.strip()
    try:
        plaintext = simplecrypt.decrypt(psw, encrypted)
    except simplecrypt.DecryptionException:
        print(psw.decode('utf8'), "- is not valid")
    else:
        print('Текст:', plaintext.decode('utf8'))
        break


"""
import simplecrypt

encrypted = open("encrypted.bin", "rb").read()
passwords = open("passwords.txt").readlines()

for p in passwords:
    p = p.strip()
    try:
        s = simplecrypt.decrypt(p, encrypted)
    except simplecrypt.DecryptionException:
        continue

    print(s.decode("utf-8"))﻿
"""
