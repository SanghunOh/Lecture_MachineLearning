#!/usr/bin/env python
# coding: utf-8

import pandas as pd

col_names=['OS', 'opcode', 'execute_command', 'malware_flag'] 
datadf = pd.read_csv("../datas/readAndwrtieCSV.csv",names=col_names, header=None) 

# Import Elasticsearch package 
from elasticsearch import Elasticsearch 
# Connect to the elastic cluster
elsearch=Elasticsearch([{'host':'localhost','port':9200}])

index_name = 'iotlog_' # Database
#index_name = 'test_idx' # Database

template={
#     "datetime": '',
#     "machine_name": '',
#     "unique_ip": '',
#     "OS": '',
#     "opcode": '',
#     "execute_command": '',
#     "malware_flag": 0, # good : 0, malware : 1
#     "running_flag": 0, # machine running rate good : 0, malware : 1
}

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

from time import sleep
flag = 1
while flag :
# while flag <= 10 :
#     flag += 1
    sleep(random.randrange(3, 15))
    range_date = pd.datetime.today()
    index_suffix = str(range_date.strftime('%Y-%m'))
    print(index_name+index_suffix, str(range_date))

    template["datetime"] = str(range_date)

    machine_name_random = random.randrange(0, machine_name_type_length)
    template["machine_name"] = machine_name_type[machine_name_random]
    template["unique_ip"] = unique_ip[machine_name_random]

    datadf_random_number = random.randrange(0, datadf_row)
    template["OS"] = datadf['OS'].iloc[datadf_random_number]
    template["opcode"] = datadf['opcode'].iloc[datadf_random_number]
    template["execute_command"] = datadf['execute_command'].iloc[datadf_random_number]
    template["malware_flag"] = int(datadf['malware_flag'].iloc[datadf_random_number])

#     template["running_flag"] = 2

    elsearch.index(index=index_name+index_suffix,body=template)