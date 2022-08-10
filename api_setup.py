#!/usr/bin/env python
# coding: utf-8

from espn_api.football import League
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import json

def getLeague(id,year,swid,s2):
    try:
        return League(id,year,swid,s2)
    except:
        return

# Importing ADP data for 2021 and defining functionality to search by name
with open("ADPdata2021.json") as f:
    adp=json.load(f)
    
def searchADPByName(name):
    try:
        result = [x for x in adp["Players"] if x["Name"]==name]
    except:
        return
    return result

def draftByTeam(xLeague,xTeam):
    xDraft = []
    xLeagueSize=len(xLeague.teams)
    for pick in xLeague.draft:
        if pick.team.team_id == xTeam.team_id:
            xPickNum=((pick.round_num - 1)*xLeagueSize)+pick.round_pick
            xAvgADP = searchADPByName(pick.playerName)
            try:
                xADP = xAvgADP[0]["AverageDraftPosition"]
            except:
                xADP= 0 
            xPick=[pick.playerName,xPickNum,xADP]
            xDraft.append(xPick)
    return xDraft

###### executable code below

# Importing league data
league_id = 49765217
year = 2021
swid='{771D2F0F-5C54-4553-8582-FCC07D235F88}'
espn_s2='AEAFCR%2F9i%2Bb3h4hoHm9sjfpXH0lhBDKmfgKEV8nU5aAocybEqSM9tlUJ1CpJtgcBN9ZKLgZM42hmCLMYICupuwIUpkZaBnDhdd886U9o8a1%2F9Sml5Vn0kSRvVGUGblNLTuxoFwBkwPyzY%2FKqdLtnqXD3DVKtATcN4Lu2VnleVW6soxz6GP7m84wgUIo5cF6b%2FcDRgg8uE8XMVmeacZGwLlouk5pdsy19MQSRjsTXcBvxZdkaA0PdId4RnS16s9Gsbbo77BdqrB4QWbiQqOx4SP4jrseK%2FVYBTDLSPmdsnVlOBw%3D%3D'
#league2021 = League(league_id,year,espn_s2,swid)
league2021 = getLeague(league_id,year,swid,espn_s2)

teamCoad = league2021.teams[15]
teams = []
for team in league2021.teams:
    teams.append(team.team_abbrev)

myDraft = draftByTeam(league2021,teamCoad)





print(myDraft)

