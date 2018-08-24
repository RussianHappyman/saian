# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.


'''





ospf_route='O     10.0.24.0/24 [100/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ospf_route=ospf_route.replace('O','OSPF')
ospf_route
ospf_route=ospf_route.replace(',','')
ospf_route
ospf_route=ospf_route.remove('[',']')
ospf_route=ospf_route.strip('[]')
ospf_route
items=ospf_route.strip().split()
items
items[2]=items[2].strip('[]')
items
print('prtocol')
print('protocol %', items[0])
print('protocol', items[0])
print("{:15} {:15}".format(items[0],items[1]))
keys = ['Protocol','Prefix','AD/Metric','Next-Hop','Last update','Outbond interface']
print("{:15} {:15}".format(keys[0],items[0]))
print("{:15} {:15}".format(keys[i],items[i] for i in range (6)))
print("{:15} {:15}".format(keys[0],items[0]))
for i in range(6):
        print("{:15} {:15}".format(keys[i],items[i]))
        for i in range(6):
                print("{:20} {:20}".format(keys[i],items[i]))
                for i in range(6):
                        print("{:20} {:20}".format(keys[i],items[i]))
                        items
                        items.remove('via')
                        items
                        for i in range(6):
                                print("{:20} {:20}".format(keys[i],items[i]))
                                %history


ip_template= '''
Protocol:                  {}
Prefix:                    {}
AD/Metric                  {}
Next_HOP                   {}
Last update                {}
Outbond intaerface         {}
'''
print(ip_template.format(protokol,prefix,ad,next_hop,last,out))


