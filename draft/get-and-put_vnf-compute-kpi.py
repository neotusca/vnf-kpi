#!/bin/python

import FortigateApi
import json
from pprint import pprint




#FOS_INFO={'fos-01':{'ip':'172.30.219.72'}, 'fos-02':{'ip':'172.30.219.73'}}
FOS_INFO={'fos-02':{'ip':'172.30.219.73'}, 'fos-01':{'ip':'172.30.219.72'}}
#print FOS_INFO, type(FOS_INFO)

ACC_INFO={'domain':'root','id':'admin','pw':'admin'}
#print ACC_INFO, type(ACC_INFO)

TOTAL_VNF_USAGE = {}



for vnf in FOS_INFO.keys():
    #print vnf, type(vnf)
    #print FOS_INFO[vnf]['ip'], type(FOS_INFO[vnf]['ip'])
    #print ACC_INFO['domain'],ACC_INFO['id'],ACC_INFO['pw'], type(ACC_INFO['domain']), type(ACC_INFO['id']), type(ACC_INFO['pw'])


    vnf_conn = FortigateApi.Fortigate(FOS_INFO[vnf]['ip'], ACC_INFO['domain'], ACC_INFO['id'], ACC_INFO['pw'])
    Response = vnf_conn.ApiGet('monitor/system/resources/')
    #Response = vnf_conn.ApiGet('monitor/firewall/session/')
    data= Response.json()

    pprint (data)
    pprint (type(data))

    #time = data['revision']
    #print "########",time

    #usage = data['results']
    #pprint (usage)
    #pprint (type(usage))


    #usage['timestamp'] = time
    #vnf_usage = {vnf:usage}
    #pprint (vnf_usage)
    #print type(vnf_usage)

    #TOTAL_VNF_USAGE[vnf] = usage    


print "--------------"
#pprint (TOTAL_VNF_USAGE)
#pprint (type(TOTAL_VNF_USAGE))

    


print "-3-------------"
#JSON_VNF_USAGE = json.dumps(TOTAL_VNF_USAGE)
#pprint (JSON_VNF_USAGE)
#pprint (type(JSON_VNF_USAGE))




