# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
with open('CAM_table.txt','r') as f:
	i=0
	s=list('')
	for line in f:
		if '.' in line:
			s += [line.split()]
s.sort()
vlan = str(input('Enter vlan number:  '))
for i in range(len(s)):
	a,b,_,c = s[i]
	if a == vlan:
		print('{}   {}   {}'.format(a,b,c))
