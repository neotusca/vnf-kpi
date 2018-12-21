#!/bin/python

import elasticsearch
from elasticsearch import helpers

import get_vnf_network_kpi
from pprint import pprint
import json
import time


def json_modify(json_str):
    dict1 = json.loads(json_str)

    for vnf in dict1.keys():
        rslt_dict = {}
        tmp = {}
        #print vnf
        #print dict1[vnf]['timestamp']
        rslt_dict['@timestamp'] = dict1[vnf]['timestamp']
        rslt_dict['vnf'] = vnf
        #print '====================='
        #print dict1[vnf].keys()
  
        cnt=0
        for port in dict1[vnf].keys():     # get port-list
            print '--------------------'
            #print dict1[vnf][port]
            #print type(dict1[vnf][port])
            if 'name' in dict1[vnf][port]:   # case normal port
                tmp['name'] = dict1[vnf][port]['name']
                tmp['ip'] = dict1[vnf][port]['ip']
                tmp['in'] = {'bytes':dict1[vnf][port]['rx_bytes'], 'packets':dict1[vnf][port]['rx_packets'], 'errors':dict1[vnf][port]['rx_errors']}
                tmp['out'] = {'bytes':dict1[vnf][port]['tx_bytes'], 'packets':dict1[vnf][port]['tx_packets'], 'errors':dict1[vnf][port]['tx_errors']}
                #print tmp

                rslt_dict['system'] = {}
                rslt_dict['system']['network'] = tmp

                cnt=cnt+1
                #print '[',cnt,']'
                #pprint (rslt_dict)
    return rslt_dict


def es_send(es_info, json):
    es_client = elasticsearch.Elasticsearch(es_info)

    print '+11++++++++++'
    print json
    print '+22++++++++++'
    docs = []
    for cnt in range(10):
        docs.append({
            '_index': 'bank_version1',
            '_type': 'account',
            '_id': 'new_id_' + str(cnt),
            '_source': {
                'state': 'NY'
            }
        })

    #_result = elasticsearch.helpers.bulk(es_client, docs)
    print '+++++++++++'
    print _result


         
    
    
def jsonfile_reading(r_file):
    f = open(r_file, 'r')
    line = f.readline()
    f.close()
    return line


    
if __name__ == "__main__":
    ''' 1. get list of vnf '''
    f_info={'fos-01':{'ip':'172.30.219.72','pw':'admin'}, 'fos-02':{'ip':'172.30.219.73','pw':'admin'}}   # using dedicated-passwd 
    a_info={'domain':'root','id':'admin'}    # using dedicated-passwd 
    ES_INFO='172.30.219.67:9200'
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
    
    print result2

    es_send(ES_INFO, result2)

    
    '''
    2. divide json & save to Elasticsearch (or Logstash)
    '''
