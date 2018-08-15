#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 11:24:48 2018

@author: MSBA 8
"""

import pandas as pd
import numpy as np
import json,urllib
from urllib.parse import urlencode
import requests
import datetime

# aquire datelist
data = pd.read_csv("~/sample_data.csv", index_col=0)
data["Date_new"]=data["Date_new"].apply(lambda x:'-'.join(x.split('/')[::-1]))
datelist = data["Date_new"].values.tolist()

datelist1, datelist2 = datelist[:150], datelist[150:] # data extraction only allows 200 times/h. split the datelist according to your need.

# single call
def get_weather(date):
    # date: (str) YYYY-MM-DD
    url = 'http://api.k780.com/'
    params = {
      'app' : 'weather.history',
      'weaid' : '2630',
      'date' : date,
      'appkey' : 'key', # input your key
      'sign' : 'sign', # input your sign
      'format' : 'json',
    }
    params = urlencode(params)
    
    jdata = requests.get('%s?%s' % (url, params)).json()
    try:
        weadata = pd.DataFrame(jdata["result"])
        print("date processed:", date)
    except KeyError:
        weadata = None
        print("date error:", date)
    
    return weadata

# test
get_weather('2018-01-22')

# Part1
findata1 = pd.DataFrame()
for date in datelist1:
    minidata = get_weather(date)
    findata1 = pd.concat([findata1, minidata], axis=0)
    
# Part2
findata2 = pd.DataFrame()
for date in datelist2:
    minidata = get_weather(date)
    findata2 = pd.concat([findata2, minidata], axis=0)
    
# concat
finaldata = pd.concat([findata1, findata2], axis=0)
finaldata.head()

finaldata.to_csv("additional_temp.csv", encoding="utf_8_sig")