# -*- coding: utf-8 -*-
'''
Задание 9.3a

Сделать копию скрипта задания 9.3.

Дополнить скрипт:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12':10,
                       'FastEthernet0/14':11,
                       'FastEthernet0/20':1 }

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
def get_int_vlan_map(name):
    access = {}
    trunk = {}
    pred_line=''
    with open(name,'r') as f:
        for line in f:
			if line.startswith('interface Fast'):
				_,a = line.strip().split()
			elif line.startswith(' switchport access'):
				_,_,_,b = line.strip().split()
				access.setdefault(a,b)
			elif 'mode access' in pred_line and 'duplex' in line:
				access.setdefault(a,'1')
			elif line.startswith(' switchport trunk allowed'):
				_,_,_,_,c =  line.strip().split()
				c = c.split(',')
				trunk.setdefault(a,c)
			pred_line=line
    print(access)
    print(trunk)
	
get_int_vlan_map('config_sw2.txt')
