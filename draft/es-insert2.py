import elasticsearch
from elasticsearch import helpers

es_client = elasticsearch.Elasticsearch("172.30.219.67:9200")

docs = []
for cnt in range(10):
    docs.append({
        '_index': 'z_index',
        '_type': 'z_type',
        '_source': {
            'state': 'NY'
        }
    })

elasticsearch.helpers.bulk(es_client, docs)


'''
{'@timestamp': u'1543400566.218132',
 'system': {'network': {'in': {'bytes': 29703348,
                               'errors': 0,
                               'packets': 570306},
                        'ip': u'0.0.0.0',
                        'name': u'port6',
                        'out': {'bytes': 90, 'errors': 0, 'packets': 1}}},
 'vnf': u'fos-01'}
'''
