# -*- coding: utf-8 -*-
'''
Задание 15.4

Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
имя файла, в котором находится вывод команды show

Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
* Interface
* IP-Address
* Status
* Protocol

Информация должна возвращаться в виде списка кортежей:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'up', 'up')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла sh_ip_int_br_2.txt.

'''
import re
import argparse

def parse_show(f_name):
    with open(f_name) as f:
        match = (re.findall('(\S+) + (\S+) +\w+ +\w+ +(up|down|administratively down) +(up|down)',f.read()))

    return match

if __name__ == "__main__":

    parser = argparse.ArgumentParser( description = 'script likes include cisco command and a little more)')
    parser.add_argument('filename', action = "store", help = 'File name')

    args = parser.parse_args()
    print(parse_show(args.filename))


