# -*- coding: utf-8 -*-
'''
Задание 5.1

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
address = '192.168.1.4/25'#input('Enter IP with mask over slash  ')
ip,mask=address.split('/')
mask=int(mask)
host=32-mask
binary_mask='1' * mask + '0' * host
oct1 = int(binary_mask[0:8],2)
oct2 = int(binary_mask[8:16],2)
oct3 = int(binary_mask[16:24],2)
oct4 = int(binary_mask[24:32],2)
ip = ip.split('.')
dec1=int(ip[0])
dec2=int(ip[1])
dec3=int(ip[2])
dec4=int(ip[3])
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
print(ip_template.format(dec1,dec2,dec3,dec4))
print(mask_template.format(mask,oct1,oct2,oct3,oct4))

