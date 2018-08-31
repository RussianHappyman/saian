# -*- coding: utf-8 -*-
'''
Задание 7.3a

Сделать копию скрипта задания 7.3.

Дополнить скрипт:
- Отсортировать вывод по номеру VLAN


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
with open('CAM_table.txt','r') as f:
	i=0
	s=list('')
	for line in f:
		if '.' in line:
			s += [line.split()]
s.sort()
for i in range(len(s)):
	a,b,_,c = s[i]
	print('{}   {}   {}'.format(a,b,c))
