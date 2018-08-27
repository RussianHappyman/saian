# -*- coding: utf-8 -*-
'''
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Enter VLAN number:'
* для trunk: 'Enter allowed VLANs:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
'''

access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]

access_type = {
	'access' : {
		'invite': 'Enter VLAN number:',
		'int_n'	: '',
		'vlan'	: '',
		'template'	: '''
interface {}
switchport mode access 
switchport access vlan {}
switchport nonegotiate 
spanning-tree portfast
spanning-tree bpduguard enable
'''
		},
	'trunk' : {
		'invite': 'Enter allowed VLANs:',
		'int_n' : '',
		'vlan' 	: '',
		'template' : '''
interface {}
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan {}
'''
		}
}
k = list(access_type.keys())
a = input('Enter interface mode {} '.format(k) )
access_type[a]['int_n'] = input('Enter interface type and number: ')
access_type[a]['vlan'] = input('{}'.format(access_type[a]['invite']))
print(access_type[a]['template'].format(access_type[a]['int_n'],access_type[a]['vlan']))
