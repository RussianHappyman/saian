# -*- coding: utf-8 -*-
'''
Задание 12.2


Функция check_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона, например,
192.168.100.1-10.

Создать функцию check_ip_availability, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.

IP-адреса могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо проверить доступность всех адресов диапазон
а включая последний.

Для упрощения задачи, можно считать, что в диапазоне всегда меняется только последни
й октет адреса.

Функция возвращает два списка:
* список доступных IP-адресов
* список недоступных IP-адресов


Для выполнения задачи можно воспользоваться функцией check_ip_addresses из задания 12.1
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