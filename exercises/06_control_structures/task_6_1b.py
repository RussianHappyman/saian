# -*- coding: utf-8 -*-
'''
Задание 6.1b

Сделать копию скрипта задания 6.1a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

correct=False
while not correct:
	ip = input('Enter IP x.x.x.x : ')
	if (len(ip.split('.'))!=4): 
		print('Incorrect IPv4 address')
	else: 
		a,b,c,d = ip.split('.')
		if ('-' in ip) or int(a) > 255 or int(b)>255 or int(c)>255 or int(c)>255 :
			print('Wrong IP range ')
		else:
			correct=True
			a = int(ip.split('.')[0])
			if a <= 223 and a>=1:	print("unicast")
			elif a>223 and a <225:	print("multicast")
			elif a==0:				print("unassigned")
			else:					print("unused")
		

