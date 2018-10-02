# -*- coding: utf-8 -*-
'''
Задание 15.2

Создать функцию return_match, которая ожидает два аргумента:
* имя файла, в котором находится вывод команды show
* регулярное выражение

Функция должна обрабатывать вывод команды show построчно и возвращать список подстрок,
которые совпали с регулярным выражением (не всю строку, где было найдено совпадение,
а только ту подстроку, которая совпала с выражением).

Проверить работу функции на примере вывода команды sh ip int br (файл sh_ip_int_br.txt).
Вывести список всех IP-адресов из вывода команды.

Соответственно, регулярное выражение должно описывать подстроку с IP-адресом (то есть, совпадением должен быть IP-адрес).


Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

'''

import re
import argparse

def incl(f_name, re_key):
    with open(f_name) as f:
       for line in f:
           match = re.search(re_key, line)
           if match:
               print(match.group())

parser = argparse.ArgumentParser(description='script likes include cisco command and a little more)')

parser.add_argument('filename', action = "store", help = 'File name')
parser.add_argument('keyword', action = "store", help = 'Key word')

args = parser.parse_args()
incl(args.filename, args.keyword)
