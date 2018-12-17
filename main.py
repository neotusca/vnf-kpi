#!/bin/python

import get_vnf_network_kpi
from pprint import pprint
import json







def json_modify(json_str):
    #pprint (json_str)
    #pprint (type(json_str))
    dict1 = json.loads(json_str)
    #pprint (dict1)
    #print dict1.keys()

    for vnf in dict1.keys():
        rslt_dict = {}
        #print vnf
        #print dict1[vnf]['timestamp']
        rslt_dict['timestamp'] = dict1[vnf]['timestamp']
        rslt_dict['vnf'] = vnf
        print '====================='
        print dict1[vnf].keys()
  
        for port in dict1[vnf].keys():
            print '--------------------'
            #print dict1[vnf][port]
            #print type(dict1[vnf][port])
            if 'name' in dict1[vnf][port]:
                for port_kpi in dict1[vnf][port].keys():
                    #print  dict1[vnf][port][port_kpi]




                #print dict1[vnf][port]['id']
                #print dict1[vnf][port]['name']
                #print dict1[vnf][port]['link']
                #print dict1[vnf][port]['ip']
            
                
        


        print '+++++++++++++++++++++'
        print rslt_dict

         

    

    




def jsonfile_reading(r_file):
    f = open(r_file, 'r')
    line = f.readline()
    f.close()
    return line
    
if __name__ == "__main__":
    ''' 1. get list of vnf '''
    f_info={'fos-01':{'ip':'172.30.219.72','pw':'admin'}, 'fos-02':{'ip':'172.30.219.73','pw':'admin'}}   # using dedicated-passwd 
    a_info={'domain':'root','id':'admin'}    # using dedicated-passwd 
    #print f_info.keys()
    #print f_info.values()
    #print f_info.items()

    ''' connect and get from fortios'''
    #result =  get_vnf_network_kpi.get_vnf_network_kpi(f_info, a_info)

    ''' connect and get from fortios'''
    result = jsonfile_reading('get_vnf_network_kpi_success.json')
    #print result
    #print type(result)  # string

    result2 = json_modify(result)
    
    
    '''
    2. divide json & save to Elasticsearch (or Logstash)
    '''
