import elasticsearch
from elasticsearch import helpers

es_client = elasticsearch.Elasticsearch("172.30.219.67:9200")

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

elasticsearch.helpers.bulk(es_client, docs)
