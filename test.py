#!/usr/bin/env python
# coding: utf-8

import numpy as np
from numpy import savetxt, loadtxt

"""
Есть две биржи: binance и okex. Нужно сделать простой словарь: 
необходимо получить список доступных инструментов с этих бирж 
и составить их в одну таблицу, в которой есть три колонки: 
- унифицированное название инструмента, 
- биржевое название binance, 
- биржевое название okex. 

Отсортировать по унифицированному названию. 
Формат csv: unify name, binance name, okex name. 
Результат должен быть выведен в терминал.
"""

# Форминование тестовых данных:
binance_list = np.array(['a', 'b', 'c', 'd'])
okex_list =np.array(['c', 'd', 'e', 'f'])

savetxt('binance_list.csv', binance_list, delimiter=',', fmt='%s')
savetxt('okex_list.csv', okex_list, delimiter=',', fmt='%s')


# Загрузка данных:
binance_list = loadtxt('binance_list.csv', delimiter=',', dtype=np.unicode_)
okex_list =loadtxt('okex_list.csv', delimiter=',', dtype=np.unicode_)

# Формирование таблицы:
a, b = set(binance_list), set(okex_list)
both = list(a & b)
binance_only = list(a.difference(b))
okex_only = list(b.difference(a))

df1 = [(i, i, i) for i in both]
df2 = [(i, i, np.nan) for i in binance_only]
df3 = [(i, np.nan, i) for i in okex_only]
values = df1 + df2 + df3

dtype = [('unify_name', np.unicode_, 16), ('binance', np.unicode_, 16), ('okex', np.unicode_, 16)]
df = np.array(values, dtype=dtype)       # structured array
df = np.sort(df, order='unify_name') 

# Выведение результата в терминал:
for item in df:
    print(*item)

