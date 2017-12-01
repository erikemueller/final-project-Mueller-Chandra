#!/usr/bin/env python

import pandas as pd
import numpy as np
import csv
import requests
#download the excel file from the UMD's GTD
dls = "http://apps.start.umd.edu/gtd/downloads/dataset/globalterrorismdb_0617dist.xlsx"
resp = requests.get(dls)
#Save file
output = open('START.xlsx', 'wb')
output.write(resp.content)
output.close()
#import downloaded file
START=pd.read_excel('START.xlsx')
#import the data for 1993 that is missing from the massive downloaded file
START1993=pd.read_excel('START1993.xlsx')
#combine both
STARTclean=START.append(START1993, ignore_index=True).sort_values('iyear')

#change names of countries and columns so that they can be better joined and merged in later actions
START1=STARTclean.replace("West Germany (FRG)", "West Germany").replace("East Germany (GDR)", "East Germany").replace("Zaire", "Democratic Republic of the Congo")
START2=START1.replace("Rhodesia", "Zimbabwe").replace("French Polynesia", "France").replace("French Guiana", "France").replace("Guadeloupe", "France").replace("Martinique", "France").replace("New Caledonia", "France").replace("Wallis and Futuna", "France")
START3=START2.replace("Macau", "Portugal").replace("International", "Yemen").replace("Slovak Republic", "Slovakia").replace("Ivory Coast", "Cote d'Ivoire").replace("People's Republic of the Congo", "Republic of the Congo")
START4=START3.replace("Antigua and Barbuda", "Antigua & Barbuda").replace("West Bank and Gaza Strip", "West Bank and Gaza")
START4.loc[(START4['country_txt'] == "Namibia") & (START4['iyear'] < 1990), 'country_txt'] = 'South Africa'
START4.loc[(START4['country_txt'] == "Soviet Union") & (START4['iyear'] == 1990), 'country_txt'] = 'Russia'
START4.loc[(START4['country_txt'] == "Hong Kong") & (START4['iyear'] < 1997), 'country_txt'] = 'United Kingdom'
START4.loc[(START4['country_txt'] == "Hong Kong") & (START4['iyear'] > 1997), 'country_txt'] = 'China'
START4.loc[(START4['country_txt'] == "West Germany") & (START4['iyear'] == 1990), 'country_txt'] = 'Germany'
START4.loc[(START4['country_txt'] == "East Germany") & (START4['iyear'] == 1990), 'country_txt'] = 'Germany'
START4.loc[(START4['country_txt'] == "East Timor") & (START4['iyear'] < 2002), 'country_txt'] = 'Indonesia'
START4.loc[(START4['country_txt'] == "Serbia-Montenegro") & (START4['iyear'] > 2006), 'country_txt'] = 'Serbia'
START4.loc[(START4['country_txt'] == "Montenegro") & (START4['iyear'] == 2001), 'country_txt'] = 'Yugoslavia'
START4.loc[(START4['country_txt'] == "Belize") & (START4['iyear'] == 1980), 'country_txt'] = 'United Kingdom'
START5 = START4.rename(columns={'country_txt': 'Country', 'iyear': 'year'})

#save a dataframe to a csv with only the columns we care about
STARTfinal = pd.DataFrame(START5, columns = ['Country', 'region_txt', 'year', 'attacktype1', 'INT_LOG', 'INT_IDEO', 'attacktype1_txt', 'nkill', 'gname', 'longitude', 'latitude', 'eventid'])
STARTfinal.to_csv('STARTfinal.csv', index=False)
