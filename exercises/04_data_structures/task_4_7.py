# -*- coding: utf-8 -*-
'''
Задание 4.7

Преобразовать MAC-адрес в двоичную строку (без двоеточий).

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

MAC = 'AAAA:BBBB:CCCC'
help(int)
help(bin)
MAC='AAAA:BBBB:CCCC'
MAC=MAC.replace(':','')
MAC
MAC=int(MAC,16)
MAC=bin(MAC)
print(MAC)
%history

