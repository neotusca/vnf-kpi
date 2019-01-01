#!/usr/bin/python

import json
from pprint import pprint

def json_modify(input):
    #print input, type(input)  # str

    dict1 = json.loads(input)
    #print dict1,type(dict1)   # dict

    rslt_list = []

    #print '=================================='
    for vnf in dict1.keys():
        #print vnf, type(vnf)
        buffer_dict = {}

        '''
        buffer_dict['@timestamp'] = dict1[vnf]['timestamp']
        buffer_dict['vnf'] = vnf
        buffer_dict['vnf_vendor'] = 'F' # vnf_vendor : Fortinet
        '''
   
        print '-----------------------------'
        for port in dict1[vnf].keys():

	    if 'timestamp' != port and 'mgmt' != port:

                buffer_dict['system'] = {}
                buffer_dict['system']['network'] = {}
                buffer_dict['system']['network']['name'] = dict1[vnf][port]['name']
                buffer_dict['system']['network']['ip']   = dict1[vnf][port]['ip']
                buffer_dict['system']['network']['in']   = {'bytes':dict1[vnf][port]['rx_bytes'], 'packets':dict1[vnf][port]['rx_packets'], 'errors':dict1[vnf][port]['rx_errors']}
                buffer_dict['system']['network']['out']  = {'bytes':dict1[vnf][port]['tx_bytes'], 'packets':dict1[vnf][port]['tx_packets'], 'errors':dict1[vnf][port]['tx_errors']}

                print '~~~~~~~~~~~~~~~~~'
                print '[%s][%s][%s]' %(vnf,port,dict1[vnf][port])
                print '[%s]' %(buffer_dict)
                


                #rslt_list.append(dict1[vnf][port])
                rslt_list.append(buffer_dict)

                print '~~~~~~~~~~~~~~~~~'
                print rslt_list


    print '#############################################################'
    pprint (rslt_list)


    
def jsonfile_reading(r_file):
    f = open(r_file, 'r')
    line = f.readline()
    f.close()
    return line


if __name__ == "__main__":
    f_info={'fos-01':{'ip':'172.30.219.72','pw':'admin'}, 'fos-02':{'ip':'172.30.219.73','pw':'admin'}}
    a_info={'domain':'root','id':'admin'}

    AA = jsonfile_reading('get_vnf_network_kpi_success.json')
    #print AA, type(AA)  # str


    BB = json_modify(AA)
