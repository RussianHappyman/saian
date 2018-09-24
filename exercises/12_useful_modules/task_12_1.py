# -*- coding: utf-8 -*-
'''
Задание 12.1

Создать функцию check_ip_addresses, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.
И возвращает два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте ping.
Адрес считается доступным, если на три ICMP-запроса пришли три ответа.

Ограничение: Все задания надо выполнять используя только пройденные темы.
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

