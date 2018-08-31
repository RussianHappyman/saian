# -*- coding: utf-8 -*-
'''
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
ignore = ['duplex', 'alias', 'Current configuration']

with open('config_sw1.txt','r') as f, open('config_sw1_cleared.txt','w+') as d :
	for line in f:
		ifprint = True
		for i in range(3): 
			if ignore[i] in line:
				ifprint = False
				break
		if not '\n' == line[0] and ifprint:
			d.write(line)
			
