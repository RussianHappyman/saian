# -*- coding: utf-8 -*-
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
ignore = ['duplex', 'alias', 'Current configuration']

with open('config_sw1.txt','r') as f:
	for line in f:
		ifprint = True
		for i in range(3): 
			if ignore[i] in line:
				ifprint = False
				break
		if not '!' in line and not '\n' == line[0] and ifprint:
			print(line[:-1])
			

