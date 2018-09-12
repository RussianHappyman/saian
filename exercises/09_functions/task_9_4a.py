# -*- coding: utf-8 -*-
'''
Задание 9.4a

Задача такая же, как и задании 9.4.
Проверить работу функции надо на примере файла config_r1.txt

Обратите внимание на конфигурационный файл.
В нем есть разделы с большей вложенностью, например, разделы:
* interface Ethernet0/3.100
* router bgp 100

Надо чтобы функция config_to_dict обрабатывала следующий уровень вложенности.
При этом, не привязываясь к конкретным разделам.
Она должна быть универсальной, и сработать, если это будут другие разделы.

Если уровня вложенности два:
* то команды верхнего уровня будут ключами словаря,
* а команды подуровней - списками

Если уровня вложенности три:
* самый вложенный уровень должен быть списком,
* а остальные - словарями.

На примере interface Ethernet0/3.100:

{'interface Ethernet0/3.100':{
               'encapsulation dot1Q 100':[],
               'xconnect 10.2.2.2 12100 encapsulation mpls':
                   ['backup peer 10.4.4.4 14100',
                    'backup delay 1 1']}}


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']


def check_ignore(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов


    Возвращает True, если в команде содержится слово из списка ignore, False - если нет

    '''
    return any(word in command for word in ignore)
   
def Parse():
	#initialize lists` variables
	res=[]
	res_dict = {}
	sub_dict = {}
	sub = []
	#initialize flags 
	flag_0 = False
	flag_1 = False
	flag_2 = False
	#open file
	f = open('config_r1.txt','r')
	#making list
	s=f.read().split('\n')
	for i in range(len(s)):
		if s[i] != '' :
			res.append(s[i])	
	#initialize counter of cycle
	i=len(res)-1
	#main cycle we will read file from the end to get right picture of commands
	while i >= 0:
		#check commands for unwanted words
		if not '!' in res[i] and not check_ignore(res[i],ignore): 
			#if line is global command
			if not res[i].startswith(' '):
				#if global command has subcommands
				if flag_1:
					res_dict.setdefault(res[i],sub_dict) # add sub to global command
					flag_1=False #turn off flag
					sub_dict = {} #and reinitialize subcommand'2 dictionary 
				#without any subcommand
				else:
					res_dict.setdefault(res[i],[])		
			#if there is sub of subcommands,then make list of theese subs
			elif res[i].startswith('  '):
				flag_2 = True #turn on flag of sub of subcommand
				sub.append(res[i])
			#if it is subcommand
			else :
				flag_1 = True # turn on flag of subcommands
				if flag_2 :	# if subcommans has subs then add subs to subcommand
					sub_dict.update({res[i]:sub})
					flag_2=False # turn off flag of sub of sub
					sub = [] #reinitialize  sub
				else:
					sub_dict.update({res[i]:[]}) # or not subs of sub
		i-=1
	print(res_dict)

Parse()
				
