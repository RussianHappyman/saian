# -*- coding: utf-8 -*-
'''
Задание 12.3


Создать функцию ip_table, которая отображает таблицу доступных и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

Функция не должна изменять списки, которые передавны ей как аргументы.
То есть, до выполнения функции и после списки должны выглядеть одинаково.

'''
import argparse
import subprocess as sp
import ipaddress
from tabulate import tabulate

def check_ip_address(ip_addr):
    reach, unreach = [], []
    for ip in ip_addr:
        reply = sp.run(['ping','-c','1','-n',str(ip)],stdout=sp.DEVNULL)
        if reply.returncode == 0:
            reach.append(ip)
        else:
            unreach.append(ip)
    return reach, unreach

def print_tab(x,y):
    ping_dict = {}
    ping_dict['reachable'] = x
    ping_dict['unreachable'] = y
    print(tabulate(ping_dict, headers='keys',tablefmt='grid'))

parser = argparse.ArgumentParser(description='Ping')

parser.add_argument('ip',action='store',help="IP or range of IP",type=str)
args = parser.parse_args()
if '-' in args.ip:
    start_ip = ipaddress.ip_address(args.ip.split('-')[0])
    if '.' in args.ip.split('-')[1]:
        end_ip = args.ip.split('-')[1].split('.')[3]
    else:
        end_ip = args.ip.split('-')[1]
    len_ip_list = int(end_ip) - int(args.ip.split('-')[0].split('.')[3])+1
    ip_list = []
    for i in range(len_ip_list):
        ip_list.append(start_ip+i)
else:
    ip_list=[args.ip]
r,u = check_ip_address(ip_list)
print_tab(r,u)