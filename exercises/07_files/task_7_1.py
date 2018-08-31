# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
ospf_template = '''
Protocol:			{}
Prefix:				{}
AD/Metric:			{}
Next-HOP:			{}
Last update:			{}
Outbond Interface		{}
'''

with open('ospf.txt','r') as f:
	for line in f:
		a = line.split('\n')[0].replace(',' ,'').replace('[','').replace(']','').replace('O','OSPF').split()
		a.remove('via')
		Prot, Pref, Metr, Next, up, out = a
		print(ospf_template.format(Prot, Pref, Metr, Next, up, out))


