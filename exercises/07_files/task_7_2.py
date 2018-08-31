# -*- coding: utf-8 -*-
'''
Задание 7.2

Создать скрипт, который будет обрабатывать конфигурационный файл config_sw1.txt:
- имя файла передается как аргумент скрипту

Скрипт должен возвращать на стандартный поток вывода команды из переданного
конфигурационного файла, исключая строки, которые начинаются с '!'.

Между строками не должно быть дополнительного символа перевода строки.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
with open('config_sw1.txt','r') as f:
	for line in f:
		if not '!' in line and not '\n' == line[0]:
			print(line[:-1])
		

'''f = open('config_sw1.txt','r')
a = f.read().replace('!','').rstrip().split('\n')
print('\n'.join(a))
	'''	
