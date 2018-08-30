# -*- coding: utf-8 -*-
'''
Задание 6.1a

Сделать копию скрипта задания 6.1.

Дополнить скрипт:
- Добавить проверку введенного IP-адреса.
- Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Incorrect IPv4 address'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
ip = input('Enter IP x.x.x.x :   ')
if (len(ip.split('.'))!=4): 
	print('Incorrect IPv4 address')
else: 
	a,b,c,d = ip.split('.')
	if ('-' in ip) or int(a) > 255 or int(b)>255 or int(c)>255 or int(c)>255 :
		print('Wrong IP range ')
	else:
		a = int(ip.split('.')[0])
		if a <= 223 and a>=1:	print("unicast")
		elif a>223 and a <225:	print("multicast")
		elif a==0:				print("unassigned")
		else:					print("unused")
