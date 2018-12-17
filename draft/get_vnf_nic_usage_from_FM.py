#!/bin/python

#import FortigateApi
import fortipy
#import fortipy.fortimanager
import json
from pprint import pprint


fg-manager = fortipy.fortimanager.FortiManager('172.30.219.69', 'admin', 'admin')
#fg-manager = forti.Forti.login('172.30.219.69', 'admin', 'admin')


fortipy.fortimanager.FortiManager.get_system_status()


#print (fg-manager, type(fg-manager))
#print (fg_fortios_01, type(fg_fortios_01))
#print type(fg_fortios_02)



print '---A---------------'
Response = fg-manager.ApiGet('monitor/system/interface')

