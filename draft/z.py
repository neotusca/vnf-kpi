#!/bin/python

import FortigateApi


print '---A---------------'
#fg-manager = FortigateApi.Fortigate('172.30.219.68', 'root', 'admin', 'admin')
fg_fortios_01 = FortigateApi.Fortigate('172.30.219.73', 'root', 'admin', 'admin')
fg_fortios_02 = FortigateApi.Fortigate('172.30.219.72', 'root', 'admin', 'admin')

#print (fg-manager, type(fg-manager))
print (fg_fortios_01, type(fg_fortios_01))
print (fg_fortios_02, type(fg_fortios_02))

print '---B---------------'
#fg.AddFwAddress('srv-A','10.1.1.1/32')
print fg_fortios_01.ApiGet('monitor/firewall/health')
print fg_fortios_02.ApiGet('monitor/firewall/health')

print '---C---------------'
#fg.GetFwAddress('srv-A')

print fg_fortios_01.ApiGet('cmdb/firewall/policy')

print '---D---------------'
print fg_fortios_02.ApiGet('cmdb/firewall/address')


print '- 00 -----------------'
print fg_fortios_02.ApiGet('monitor/system/available-interfaces/select')

print '- 01 -----------------'
print fg_fortios_02.ApiGet('monitor/system/fortimanager/status')

print '- 02 -----------------'
print fg_fortios_02.ApiGet('monitor/system/ha-statistics/select')

print '- 03 -----------------'
print fg_fortios_02.ApiGet('monitor/system/ha-history/select')

print '- 04 -----------------'
print fg_fortios_02.ApiGet('monitor/system/ha-peer/select')

print '- 05 -----------------'
print fg_fortios_02.ApiGet('monitor/system/link-monitor/select')

print '- 06 -----------------'
print fg_fortios_02.ApiGet('monitor/system/resource/usage')

print '- 07 -----------------'
print fg_fortios_02.ApiGet('monitor/system/interface')

print '- 08 -----------------'
print fg_fortios_02.ApiGet('monitor/system/interface/select')

print '- 07 -----------------'
print fg_fortios_02.ApiGet('monitor/system/interface/select/port1')
