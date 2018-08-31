# -*- coding: utf-8 -*-
'''
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
from sys import argv

ignore = ['duplex', 'alias', 'Current configuration']

in_f, out_f = argv[1:]
with open(in_f,'r') as f, open(out_f,'w+') as d :
	for line in f:
		ifprint = True
		for i in range(3): 
			if ignore[i] in line:
				ifprint = False
				break
		if not '\n' == line[0] and ifprint:
			d.write(line)
			
