# -*- coding: utf-8 -*-
'''
Задание 5.1b

Преобразовать скрипт из задания 5.1a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
from sys import argv
#address = '192.168.1.40/28'#input('Enter IP with mask over slash  ')
ip,mask= argv[1:]
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
