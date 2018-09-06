# -*- coding: utf-8 -*-
'''
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает два объекта:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12':10,
 'FastEthernet0/14':11,
 'FastEthernet0/16':17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1':[10,20],
 'FastEthernet0/2':[11,30],
 'FastEthernet0/4':[17]}

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
def get_int_vlan_map():
    access = {}
    trunk = {}
    with open('config_sw1.txt','r') as f:
        for line in f:
			if line.startswith('interface Fast'):
				_,a = line.strip().split()
			elif line.startswith(' switchport access'):
				_,_,_,b = line.strip().split()
				access.setdefault(a,b)
			elif line.startswith(' switchport trunk allowed'):
				_,_,_,_,c =  line.strip().split()
				c = c.split(',')
				trunk.setdefault(a,c)
    print(access)
    print(trunk)
	
get_int_vlan_map()
