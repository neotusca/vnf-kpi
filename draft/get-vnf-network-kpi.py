#!/bin/python

import FortigateApi
import json
from pprint import pprint


''' using common-passwd
#FOS_INFO={'fos-01':{'ip':'172.30.219.72'}, 'fos-02':{'ip':'172.30.219.73'}}  # using common-passwd
#ACC_INFO={'domain':'root','id':'admin','pw':'admin'}   # using common-passwd
'''
''' using dedicated-passwd '''
FOS_INFO={'fos-01':{'ip':'172.30.219.72','pw':'admin'}, 'fos-02':{'ip':'172.30.219.73','pw':''}}   # using dedicated-passwd 
ACC_INFO={'domain':'root','id':'admin'}    # using dedicated-passwd 

TOTAL_VNF_USAGE = {}



for vnf in FOS_INFO.keys():
    #print vnf, type(vnf)
    '''  using common-passwd
    print FOS_INFO[vnf]['ip'], type(FOS_INFO[vnf]['ip'])
    print ACC_INFO['domain'],ACC_INFO['id'],ACC_INFO['pw'], type(ACC_INFO['domain']), type(ACC_INFO['id']), type(ACC_INFO['pw'])
    '''
    '''  using dedicated-passwd  
    print FOS_INFO[vnf]['ip'], FOS_INFO[vnf]['pw'], type(FOS_INFO[vnf]['ip']), type(FOS_INFO[vnf]['pw'])
    print ACC_INFO['domain'],ACC_INFO['id'], type(ACC_INFO['domain']), type(ACC_INFO['id'])
    '''
    
    #vnf_conn = FortigateApi.Fortigate(FOS_INFO[vnf]['ip'], ACC_INFO['domain'], ACC_INFO['id'], ACC_INFO['pw'])
    vnf_conn = FortigateApi.Fortigate(FOS_INFO[vnf]['ip'], ACC_INFO['domain'], ACC_INFO['id'], FOS_INFO[vnf]['pw'])

    Response = vnf_conn.ApiGet('monitor/system/interface')
    #pprint (Response)

    data= Response.json()

    time = data['revision']
    #print "########",time

    usage = data['results']
    #pprint (usage)
    #pprint (type(usage))

    usage['timestamp'] = time
    vnf_usage = {vnf:usage}
    #pprint (vnf_usage)
    #print type(vnf_usage)

    TOTAL_VNF_USAGE[vnf] = usage    


#pprint (TOTAL_VNF_USAGE)
#pprint (type(TOTAL_VNF_USAGE))


JSON_VNF_USAGE = json.dumps(TOTAL_VNF_USAGE)
pprint (JSON_VNF_USAGE)
#pprint (type(JSON_VNF_USAGE))



'''
##### structure of process
1. get list-of-vnf (from FortiManager|NSO)
  - connect API
  - get data

2. retrive vnf-id from list-of-vnf
  - for syntax

'''
