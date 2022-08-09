#!/usr/bin/env python
# coding: utf-8

# In[1]:


from espn_api.football import League
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import json


# Importing league data

# In[2]:


league_id = 49765217
year = 2021
swid='{771D2F0F-5C54-4553-8582-FCC07D235F88}'
espn_s2='AEAFCR%2F9i%2Bb3h4hoHm9sjfpXH0lhBDKmfgKEV8nU5aAocybEqSM9tlUJ1CpJtgcBN9ZKLgZM42hmCLMYICupuwIUpkZaBnDhdd886U9o8a1%2F9Sml5Vn0kSRvVGUGblNLTuxoFwBkwPyzY%2FKqdLtnqXD3DVKtATcN4Lu2VnleVW6soxz6GP7m84wgUIo5cF6b%2FcDRgg8uE8XMVmeacZGwLlouk5pdsy19MQSRjsTXcBvxZdkaA0PdId4RnS16s9Gsbbo77BdqrB4QWbiQqOx4SP4jrseK%2FVYBTDLSPmdsnVlOBw%3D%3D'
league = League(league_id,year,espn_s2,swid)


# Importing ADP data for 2021 and defining functionality to search by name

# In[3]:


with open("ADPdata2021.json") as f:
    adp=json.load(f)
    
def searchADPByName(name):
    try:
        result = [x for x in adp["Players"] if x["Name"]==name]
    except:
        return
    return result


# attempting to collect some data and plot

# In[4]:


teamCoad = league.teams[15]
teams = []
for team in league.teams:
    teams.append(team.team_abbrev)


# In[7]:


def draftByTeam(xteam):
    draft=[]
    for pick in league.draft:
        if pick.team == xteam:
            draftPick=((pick.round_num - 1)*16)+pick.round_pick
            onePick=(pick.playerName,draftPick)
            draft.append(onePick)
    return draft


# In[8]:


myDraft = draftByTeam(teamCoad)
averages=[]
for pick in myDraft:
    avgADP = searchADPByName(pick[0])
    try:
        averages.append([avgADP[0]["Name"],avgADP[0]["AverageDraftPosition"],pick[1]])
    except:
        print("Player not found")


# In[ ]:




