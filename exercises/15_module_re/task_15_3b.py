# -*- coding: utf-8 -*-
'''
Задание 15.3b

Проверить работу функции parse_cfg из задания 15.3a на конфигурации config_r2.txt.

Обратите внимание, что на интерфейсе e0/1 назначены два IP-адреса:
interface Ethernet0/1
 ip address 10.255.2.2 255.255.255.0
 ip address 10.254.2.2 255.255.255.0 secondary

А в словаре, который возвращает функция parse_cfg, интерфейсу Ethernet0/1
соответствует только один из них (второй).

Переделайте функцию parse_cfg из задания 15.3a таким образом,
чтобы она возвращала список кортежей для каждого интерфейса.
Если на интерфейсе назначен только один адрес, в списке будет один кортеж.
Если же на интерфейсе настроены несколько IP-адресов, то в списке будет несколько кортежей.

Проверьте функцию на конфигурации config_r2.txt и убедитесь, что интерфейсу
Ethernet0/1 соответствует список из двух кортежей.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

'''
import re
import argparse

def incl(f_name):
    regex = ' ip address (\S+) (\S+)'
    res_dict = {}
    fl1 = False
    with open(f_name) as f:
        for line in f:
            if line.startswith('interface'):
                fl1 = True
                match = re.match('(interface \S+)',line)
            elif line.startswith(' ip address '):
                if fl1:
                    res_dict[match.group()] = tuple((re.match(regex, line).group(1),
                                                     re.match(regex, line).group(2)))
                    temp = res_dict[match.group()]
                    fl1 = False
                else:
                    res_dict[match.group()] = [(temp),(re.match(regex, line).group(1),
                                                       re.match(regex, line).group(2))]
    print(res_dict)

parser = argparse.ArgumentParser(description='script likes include cisco command and a little more)')
parser.add_argument('filename', action = "store", help = 'File name')

args = parser.parse_args()
incl(args.filename)