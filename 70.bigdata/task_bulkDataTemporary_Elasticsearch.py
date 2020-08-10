#!/usr/bin/env python
# coding: utf-8

import pandas as pd

col_names=['OS', 'opcode', 'execute_command', 'malware_flag'] 
datadf = pd.read_csv("../datas/readAndwrtieCSV.csv",names=col_names, header=None) 


# Import Elasticsearch package 
from elasticsearch import Elasticsearch 

index_name = 'iotlog_' # Database
documenttype_name = '' # Type of the document

template={}

import random
from datetime import datetime

machine_name_type = ['Google Home Voice Controller',
            'Amazon Echo Plus Voice Controller',
            'Amazon Dash Button',
            'August Doorbell Cam',
            'August Smart Lock',
            'Kuri Mobile Robot',
            'Belkin WeMo Smart Light Switch',
            'Footbot Air Quality Monitor']

machine_name_type_length = len(machine_name_type)-1

unique_ip = ['211.201.165.134',
            '201.101.161.31',
            '251.121.161.33',
            '221.201.164.34',
            '111.211.162.35',
            '101.201.165.36',
            '121.101.161.37',
            '141.202.162.38',]

datadf_row = datadf.shape[0] - 1

from datetime import date

start_day = date(2019, 1, 1)
end_day = date(2019, 3, 1)
templage_periods = end_day - start_day
print(templage_periods.days)

template_count_start = 50
template_count_end = 100

template_date = pd.date_range(end = end_day, periods = templage_periods.days+1).to_pydatetime().tolist()

import datetime
start_time = datetime.datetime.now()
print('start time : ' + str(start_time))

# Connect to the elastic cluster
#elsearch=Elasticsearch([{'host':'localhost','port':9200}],timeout=30, max_retries=3, retry_on_timeout=True)
elsearch=Elasticsearch([{'host':'localhost','port':9200}])
# only wait for 1 second, regardless of the client's default
# elsearch.cluster.health(wait_for_status='yellow', request_timeout=10)
    
for range_date in template_date:
#     index_name = str(range_date.strftime('%Y-%m-%d'))
    index_suffix = str(range_date.strftime('%Y-%m'))
    template_count = random.randrange(template_count_start, template_count_end)
    
    print(index_name, index_suffix, template_count)
    documenttype_name = index_suffix
    #body_list = []
    for i in range(0,template_count):
        template["datetime"] = str(range_date)

        machine_name_random = random.randrange(0, machine_name_type_length)
        template["machine_name"] = machine_name_type[machine_name_random]
        template["unique_ip"] = unique_ip[machine_name_random]

        datadf_random_number = random.randrange(0, datadf_row)
        template["OS"] = datadf['OS'].iloc[datadf_random_number]
        template["opcode"] = datadf['opcode'].iloc[datadf_random_number]
        template["execute_command"] = datadf['execute_command'].iloc[datadf_random_number]
        template["malware_flag"] = int(datadf['malware_flag'].iloc[datadf_random_number])

        template["running_flag"] = random.randrange(0, 1)

#         elsearch.index(index=index_name,doc_type=documenttype_name,body=template)
        elsearch.index(index=index_name+index_suffix,body=template)
#         print('-------',str(range_date))

print('end time : ' + str(datetime.datetime.now()))
print('running time : ' + str(datetime.datetime.now() - start_time))
