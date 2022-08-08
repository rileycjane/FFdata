#!/usr/bin/env python
# coding: utf-8

# In[2]:


from espn_api.football import League
import numpy as np
import pandas as pd
import json


# Importing league data

# In[3]:


league_id = 49765217
year = 2021
swid='{771D2F0F-5C54-4553-8582-FCC07D235F88}'
espn_s2='AEAFCR%2F9i%2Bb3h4hoHm9sjfpXH0lhBDKmfgKEV8nU5aAocybEqSM9tlUJ1CpJtgcBN9ZKLgZM42hmCLMYICupuwIUpkZaBnDhdd886U9o8a1%2F9Sml5Vn0kSRvVGUGblNLTuxoFwBkwPyzY%2FKqdLtnqXD3DVKtATcN4Lu2VnleVW6soxz6GP7m84wgUIo5cF6b%2FcDRgg8uE8XMVmeacZGwLlouk5pdsy19MQSRjsTXcBvxZdkaA0PdId4RnS16s9Gsbbo77BdqrB4QWbiQqOx4SP4jrseK%2FVYBTDLSPmdsnVlOBw%3D%3D'
league = League(league_id,year,espn_s2,swid)


# Importing ADP data for 2021 and defining functionality to search by name

# In[4]:


with open("ADPdata2021.json") as f:
    adp=json.load(f)
    
def searchByName(name):
    result = [x for x in adp["Players"] if x["Name"]==name]
    return result


# In[ ]:




