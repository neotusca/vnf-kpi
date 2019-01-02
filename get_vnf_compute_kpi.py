#!/bin/python

import FortigateApi
import json
import time
from pprint import pprint

TOTAL_VNF_USAGE = {}

def get_vnf_compute_kpi(FOS_INFO, ACC_INFO):
    usage={}

    for vnf in FOS_INFO.keys():
        
        vnf_conn = FortigateApi.Fortigate(FOS_INFO[vnf]['ip'], ACC_INFO['domain'], ACC_INFO['id'], FOS_INFO[vnf]['pw'])
    
        Response = vnf_conn.ApiGet('monitor/system/resource/usage')    # usage history
    
        if Response.status_code != 200:
            ''' abnormal process '''
            #print 'Response.status_code : [',Response.status_code,']'
            #print "Not valid connect to forti-os. Check the connection to [",vnf,"], please.."
            usage['timestamp'] = str(time.time())
            usage['message'] = 'Invalid connect to forti-os'

        else:
            ''' normal process '''
            data = Response.json()
            #pprint (data)
            #print type(data)  # dict

            usage['cpu']       = data['results']['cpu'][0]['current']
            usage['mem']       = data['results']['mem'][0]['current']
            usage['disk']      = data['results']['disk'][0]['current']
            usage['session']   = data['results']['session'][0]['current']

            print '+1+++++++++++++++++++++'
            print vnf, usage, type(usage)

        
            TOTAL_VNF_USAGE[vnf] = {}
            TOTAL_VNF_USAGE[vnf].update(usage)    # dictionary  not work

        print '+2+++++++++++++++++++++'
        print TOTAL_VNF_USAGE

        #pprint (TOTAL_VNF_USAGE) # dict
        JSON_VNF_USAGE = json.dumps(TOTAL_VNF_USAGE)

    #pprint (JSON_VNF_USAGE)
    #pprint (type(JSON_VNF_USAGE))
    return JSON_VNF_USAGE
    
    
    
if __name__ == "__main__":
    f_info={'fos-01':{'ip':'172.30.219.72','pw':'admin'}, 'fos-02':{'ip':'172.30.219.73','pw':'admin'}}   # using dedicated-passwd 
    a_info={'domain':'root','id':'admin'}    # using dedicated-passwd 

    result =  get_vnf_compute_kpi(f_info, a_info)
    #print result
    pprint (result)

    
