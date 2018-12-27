#!/bin/python

#import elasticsearch
from elasticsearch import Elasticsearch
from elasticsearch import helpers
from pprint import pprint
import json
import time

import get_vnf_network_kpi


def json_modify(json_str):
    dict1 = json.loads(json_str)   # json to dictionary
    rslt_list = []
    #rslt_dict = {}

    print '~~1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    for vnf in dict1.keys():       # get vnf-name
        buffer_dict = {}
        tmp = {}
        buffer_dict['@timestamp'] = dict1[vnf]['timestamp']
        buffer_dict['vnf'] = vnf
        buffer_dict['vnf_vendor'] = 'F' # vnf_vendor : Fortinet
        #print buffer_dict

        print '~~2~~~~~~~~~~~~~~~~~~~~~~~~~~'
        for port in dict1[vnf].keys():     # get port-list
            #print '=',port,'=',dict1[vnf][port],'='
            #print type(dict1[vnf][port])
            if 'name' in dict1[vnf][port]:   # case normal port
                #print '#',vnf,'#',port,'#',dict1[vnf][port]
                tmp['name'] = dict1[vnf][port]['name']
                tmp['ip'] = dict1[vnf][port]['ip']
                tmp['in'] = {'bytes':dict1[vnf][port]['rx_bytes'], 'packets':dict1[vnf][port]['rx_packets'], 'errors':dict1[vnf][port]['rx_errors']}
                tmp['out'] = {'bytes':dict1[vnf][port]['tx_bytes'], 'packets':dict1[vnf][port]['tx_packets'], 'errors':dict1[vnf][port]['tx_errors']}
                #print tmp

                buffer_dict['system'] = {}
                buffer_dict['system']['network'] = tmp

                #pprint (buffer_dict)
                #print '[',vnf,'][',port,']',buffer_dict, type(buffer_dict)
                rslt_list.append(buffer_dict)   # add dict in list
                print '~~3~~~~~~~~~~~~~~~~~~~~'
                print rslt_list

    print '~~4~~~~~~~~~~~~~~~~~~~~'
    print rslt_list
    return rslt_list


def es_send(es_info, input):
    print "===es_send=============="
    #print '[',es_info, type(es_info)
    print "input : "
    print input, type(input)  # list, not  dict

    json1 = json.dumps(input)
    print "---"
    print json1,type(json1)  # string

    #es_client = elasticsearch.Elasticsearch(es_info)
    es_client = Elasticsearch(es_info)
    print es_client, type(es_client)

    buffer_dict1 = {}
    buffer_dict1['_index'] = 'vnf-kpi4'
    buffer_dict1['_type'] = 'metricsets' #({'_index':'vnf-kpi4','_type':'metricsets','_source':
    
    #rslt_dict1 = {}
    rslt_list1 = []
    str1 = ""

    print "------------------------"
    cnt=1
    #for record in input.values():

    for record in input:
        print record
        buffer_dict1['_source'] = record
        #print cnt, record

        #str1 = str1+json.dumps(record)
        #print cnt, str1, type(str1)
        print buffer_dict1,type(buffer_dict1)
        rslt_list1.append(buffer_dict1)
        cnt=cnt+1

    print '+++++++++++'
    #print str1, type(str1)
    #print rslt_list1, type(rslt_list1)
    pprint(rslt_list1)

    _result = helpers.bulk(es_client, rslt_list1)    #   not string, be list
    #_result = helpers.bulk(es_client, json1)
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

    ''' connect and get from fortios'''
    result =  get_vnf_network_kpi.get_vnf_network_kpi(f_info, a_info)

    ''' connect and get from fortios'''
    #result = jsonfile_reading('get_vnf_network_kpi_success.json')
    print '=1=========='
    print result, type(result)  # string

    result2 = json_modify(result)
    
    print '=2=========='
    #pprint(result2)
    print result2, type(result2)
    #print '=2=========='

    result3 = es_send(ES_INFO, result2)
    print '=3=========='
    print result3, type(result3)

    
    '''
    2. divide json & save to Elasticsearch (or Logstash)
    '''
