#!/bin/python

import FortigateApi
import json
from pprint import pprint


#fg-manager = FortigateApi.Fortigate('172.30.219.68', 'root', 'admin', 'admin')
fg_fortios_01 = FortigateApi.Fortigate('172.30.219.72', 'root', 'admin', 'admin')
#fg_fortios_02 = FortigateApi.Fortigate('172.30.219.73', 'root', 'admin', 'admin')
fg_fortios_02 = FortigateApi.Fortigate('172.30.219.73', 'root', 'admin', '')

#print (fg-manager, type(fg-manager))
#print (fg_fortios_01, type(fg_fortios_01))
#print type(fg_fortios_02)



print '---A---------------'
Response_1 = fg_fortios_01.ApiGet('monitor/system/interface')

data_1 = Response_1.json()
#print data, type(data)


time = data_1['revision']
print "########",time

usage = data_1['results']
pprint (usage)




print '---B---------------'
Response_2 = fg_fortios_02.ApiGet('monitor/system/interface')

data_2 = Response_2.json()
#print data_2, type(data_2)


time = data_2['revision']
print "########",time

usage = data_2['results']
pprint (usage)
#pprint (type(usage))

list_port = usage.keys()
#print list_port, type(list_port) <-- list


for port  in list_port:
  #print port
  print usage[port]
  pprint (usage[port])
  del usage[port]['alias']
  del usage[port]['duplex']
  del usage[port]['link']
  del usage[port]['mac']
  del usage[port]['mask']
  del usage[port]['speed']
  pprint (usage[port])


print "======================================"


{u'alias': u'',
 u'duplex': 1,
 u'id': u'port1',
 u'ip': u'192.168.122.4',
 u'link': True,
 u'mac': u'00:00:00:00:00:00',
 u'mask': 24,
 u'name': u'port1',
 u'rx_bytes': 88204349,
 u'rx_errors': 0,
 u'rx_packets': 1694277,
 u'speed': 10000.0,
 u'tx_bytes': 147297,
 u'tx_errors': 0,
 u'tx_packets': 2428}
