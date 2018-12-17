#!/bin/python

import FortigateApi
import json
import time
from pprint import pprint

TOTAL_VNF_USAGE = {}

def get_vnf_network_kpi(FOS_INFO, ACC_INFO):
    usage={}

    for vnf in FOS_INFO.keys():
        #print vnf, type(vnf)
        '''  using dedicated-passwd  
        print FOS_INFO[vnf]['ip'], FOS_INFO[vnf]['pw'], type(FOS_INFO[vnf]['ip']), type(FOS_INFO[vnf]['pw'])
        print ACC_INFO['domain'],ACC_INFO['id'], type(ACC_INFO['domain']), type(ACC_INFO['id'])
        '''
        
        #vnf_conn = FortigateApi.Fortigate(FOS_INFO[vnf]['ip'], ACC_INFO['domain'], ACC_INFO['id'], ACC_INFO['pw'])
        vnf_conn = FortigateApi.Fortigate(FOS_INFO[vnf]['ip'], ACC_INFO['domain'], ACC_INFO['id'], FOS_INFO[vnf]['pw'])
    
        Response = vnf_conn.ApiGet('monitor/system/interface')
        #print '3=',Response.status_code,'=='
    
        if Response.status_code != 200:
            ''' abnormal process '''
            #print 'Response.status_code : [',Response.status_code,']'
            #print "Not valid connect to forti-os. Check the connection to [",vnf,"], please.."
            usage['timestamp'] = str(time.time())
            usage['message'] = 'Invalid connect to forti-os'

        else:
            ''' normal process '''
            data = Response.json()

            timestamp = data['revision']
            usage = data['results']
            usage['timestamp'] = timestamp
        
        TOTAL_VNF_USAGE[vnf] = usage    
        #pprint (TOTAL_VNF_USAGE) # dict
        JSON_VNF_USAGE = json.dumps(TOTAL_VNF_USAGE)

    #pprint (JSON_VNF_USAGE)
    #pprint (type(JSON_VNF_USAGE))
    return JSON_VNF_USAGE
    
    
    
if __name__ == "__main__":
    f_info={'fos-01':{'ip':'172.30.219.72','pw':'admin'}, 'fos-02':{'ip':'172.30.219.73','pw':'admin'}}   # using dedicated-passwd 
    a_info={'domain':'root','id':'admin'}    # using dedicated-passwd 

    result =  get_vnf_network_kpi(f_info, a_info)
    print result

    
