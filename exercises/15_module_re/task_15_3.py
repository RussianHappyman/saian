# -*- coding: utf-8 -*-
'''
Задание 15.3

Создать функцию parse_cfg, которая ожидает как аргумент имя файла,
в котором находится конфигурация устройства.

Функция должна обрабатывать конфигурацию и возвращать IP-адреса и маски,
которые настроены на интерфейсах, в виде списка кортежей:
* первый элемент кортежа - IP-адрес
* второй элемент кортежа - маска

Например (взяты произвольные адреса):
[('10.0.1.1', '255.255.255.0'), ('10.0.2.1', '255.255.255.0')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.


Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

'''

import re
import argparse

def incl(f_name):
    res = []
    with open(f_name) as f:
       for line in f:
           match = re.search(' ip address ((\d+\.?){4}) (\d+\.+\d+\.+\d+\.+\d+)',line)
           if match:
               res.append((match.group(1),match.group(3)))
    print(res)
parser = argparse.ArgumentParser(description='script likes include cisco command and a little more)')

parser.add_argument('filename', action = "store", help = 'File name')

args = parser.parse_args()
incl(args.filename)