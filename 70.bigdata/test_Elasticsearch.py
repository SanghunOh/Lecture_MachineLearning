#!/usr/bin/env python
# coding: utf-8

import pandas as pd

# col_names=['OS', 'opcode', 'execute_command', 'malware_flag'] 
# datadf = pd.read_csv("../datas/readAndwrtieCSV.csv",names=col_names, header=None) 


# Import Elasticsearch package 
from elasticsearch import Elasticsearch 

index_prefix = 'iotlog_' # Database

elsearch = Elasticsearch([{'host':'localhost','port':9200}])

query_body = {
  "query": {
    "bool": {
      "must_not": {
        "exists": {
          "field": "running_flag"
        }
      }
    }
  }
}
print('query_body : ',query_body)

flag = 1
# while flag :
while flag <= 2 :
    flag += 1
    range_date = pd.datetime.today()
    index_suffix = str(range_date.strftime('%Y-%m'))

    index_name = index_prefix + index_suffix
    result = elsearch.search(index=index_name,body=query_body)

    print("Got %d Hits:" % result['hits']['total']['value'])

    # print("%d documents found:" % result['hits']['total'])
    for hit in result['hits']['hits']:
        print(hit["_source"]['datetime'])        
        elsearch.update(index=index_name, 
                        id=hit["_id"],
                         body={
                             'doc':{'running_flag': hit["_source"]["malware_flag"]}
                         }
                     )        
# print('end time : ' + str(datetime.datetime.now()))
# print('running time : ' + str(datetime.datetime.now() - start_time))
