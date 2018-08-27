# -*- coding: utf-8 -*-
'''
Задание 5.1a

Всё, как в задании 5.1. Но, если пользователь ввел адрес хоста, а не адрес сети,
то надо адрес хоста преобразовать в адрес сети и вывести адрес сети и маску, как в задании 5.1.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.1/30 - хост из сети 10.0.5.0/30

Если пользователь ввел адрес 10.0.1.1/24,
вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
address = '192.168.1.40/28'#input('Enter IP with mask over slash  ')
ip,mask=address.split('/')
mask=int(mask)
host=32-mask
binary_mask='1' * mask + '0' * host
moct1 = int(binary_mask[0:8],2)
moct2 = int(binary_mask[8:16],2)
moct3 = int(binary_mask[16:24],2)
moct4 = int(binary_mask[24:32],2)
ip = ip.split('.')
dec1=int(ip[0])
dec2=int(ip[1])
dec3=int(ip[2])
dec4=int(ip[3])
binary_ip = '{:08b}{:08b}{:08b}{:08b}'.format(dec1,dec2,dec3,dec4)
binary_net = binary_ip[:mask]+'0'*host
noct1 = int(binary_net[0:8],2)
noct2 = int(binary_net[8:16],2)
noct3 = int(binary_net[16:24],2)
noct4 = int(binary_net[24:32],2)

ip_template='''
    Network:
    {0:<10}{1:<10}{2:<10}{3:<10}
    {0:08b}  {1:08b}  {2:08b}  {3:08b} 
'''
mask_template='''
    Mask:
    /{0}
    {1:<10}{2:<10}{3:<10}{4:<10}
    {1:08b}  {2:08b}  {3:08b}  {4:08b} 
'''
print(ip_template.format(noct1,noct2,noct3,noct4))
print(mask_template.format(mask,moct1,moct2,moct3,moct4))
