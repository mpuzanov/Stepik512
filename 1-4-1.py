# -*- coding: utf-8 -*-
'''
Реализуйте программу, которая будет эмулировать работу с пространствами имен. 
Необходимо реализовать поддержку создания пространств имен и добавление в них переменных.
'''
def fun_create(namesp, var):
    #print('create',namesp, var)
    namespaces[namesp]=var
    variables[namesp]=[]
def fun_add(namesp, var):
    #print('add',namesp, var)
    variables[namesp].append(var)
def fun_get(namesp, var):
    #print('get',namesp, var)
    #print(variables[namesp],var)
    if namesp in variables and var in variables[namesp]:
        print(namesp)
    else: 
        #print('не нашли:',namesp)
        if namesp in namespaces and namespaces[namesp] in namespaces:
            fun_get(namespaces[namesp], var)
        elif namesp not in variables:
            fun_get('global', var)
        else:
            print('None')
    
n = int(input())
namespaces = {'global': None} # ключ - namespace. значение - parent
variables = {'global': []} # ключ - namespace. значение - множество переменных
for i in range(n):
    cmd, namesp, arg = input().split() 
    #print(cmd, namesp, arg)
    if cmd == 'create':
        fun_create(namesp, arg)
    if cmd == 'add':
        fun_add(namesp, arg)
    if cmd == 'get':
        fun_get(namesp, arg)

#print(namespaces)  
#print(variables)  
'''
n = int(input())

parent = {"global": None}
vs = {"global": set()}

for _ in range(n):
    t, fst, snd = input().split()
    if t == "create":
        parent[fst] = snd
        vs[fst] = set()
    elif t == "add":
        vs[fst].add(snd)
    else:  # t == get
        while fst is not None:
            if snd in vs[fst]:
                break
            fst = parent[fst]
        print(fst)
'''        