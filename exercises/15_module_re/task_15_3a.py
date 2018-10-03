# -*- coding: utf-8 -*-
'''
Задание 15.3a

Переделать функцию parse_cfg из задания 15.3 таким образом, чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

Например (взяты произвольные адреса):
{'FastEthernet0/1':('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2':('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

'''
import re
import argparse

def incl(f_name):
    res_dict = {}
    fl1 = False
    with open(f_name) as f:
        for line in f:
            if line.startswith('interface'):
                fl1 = True
                match = re.match('(interface \S+)',line)
            elif line.startswith(' ip address ') and fl1 :
                res_dict[match.group()] = (re.match(' ip address (\S+) (\S+)', line).group(1), re.match(' ip address (\S+) (\S+)',line).group(2))
                fl1 = False
    print(res_dict)

parser = argparse.ArgumentParser(description='script likes include cisco command and a little more)')
parser.add_argument('filename', action = "store", help = 'File name')

args = parser.parse_args()
incl(args.filename)