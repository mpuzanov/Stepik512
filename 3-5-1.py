# coding: utf-8
"""
Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго с 2001 года по настоящее время.

Одним из атрибутов преступления является его тип – Primary Type.

Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.
"""
import csv
# import datetime

dict_crimes = {}
with open("Crimes.csv", 'rt') as f:
    cin = csv.DictReader(f)
    for row in cin:
        # d1 = datetime.datetime.strptime(row["Date"], '%m/%d/%Y %H:%M:%S %p')  # 10/01/2002 12:47:08 PM
        # if d1.year == 2015:
        if '2015' in row["Date"]:
            dict_crimes[row["Primary Type"]] = dict_crimes.get(row["Primary Type"], 0) + 1
            # print(row["Date"], d1, row["Primary Type"])



# with open("Crimes.csv", 'rt') as f:
#     cin = csv.reader(f)
#     for row in cin:
#         # row[5] - имя ключа
#         # row[2] нужен только 2015 год
#         if
#         dict_crimes[row[5]] = dict_crimes.get(row[5], 0) + 1
#         # print(row[5])

# Отсортирум словарь по значению
dict_crimes = sorted(dict_crimes, key=dict_crimes.get, reverse=True)
print(dict_crimes[0])

"""
import csv

with open("Crimes.csv") as fi:
    reader = csv.reader(fi)
    next(reader)
    crime_cnt = dict()
    for row in reader:
        year = row[2][6:10]
        if year == "2015":
            crime_type = row[5]
            if crime_type not in crime_cnt:
                crime_cnt[crime_type] = 0
            crime_cnt[crime_type] += 1

a = list(map(lambda x: (crime_cnt[x], x), crime_cnt))
a.sort(key=lambda x: -x[0])

print(a[0][1])

=================================================
import csv
crimes = [row[5] for row in csv.reader(open("Crimes.csv"))]
print(max(set(crimes), key=lambda x: crimes.count(x)))

"""