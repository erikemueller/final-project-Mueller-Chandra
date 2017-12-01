#!/usr/bin/env python

import pandas as pd
import numpy as np
import csv
import requests
#download the excel file from the UMD's GTD
dls = "https://uofi.box.com/shared/static/d27425539c9d662a7041.xls"
resp = requests.get(dls)
#Save file
output = open('Cheibub.xls', 'wb')
output.write(resp.content)
output.close()
#import downloaded file
Cheibub=pd.read_excel('Cheibub.xls')

#cleaning data for merging
Cheibub1=Cheibub.replace("United States of America", "United States").replace("Germany, East", "East Germany").replace("Germany, West", "West Germany")
Cheibub2=Cheibub1.replace("Democratic Republic of the Congo (Zaire, Congo-Kinshasha)", "Democratic Republic of the Congo").replace("Viet Nam", "Vietnam").replace("Vietnam, South", "South Vietnam").replace("Vietnam, North", "North Vietnam")
Cheibub3=Cheibub2.replace("Yemen PDR (South)", "South Yemen").replace("Yemen Arab Republic", "North Yemen").replace("Serbia and Montenegro", "Serbia-Montenegro").replace("Russian Federation", "Russia")
Cheibub4=Cheibub3.replace("Bosnia and Herzegovina", "Bosnia-Herzegovina").replace("U.S.S.R.", "Soviet Union").replace("Libyan Arab Jamahiriya", "Libya")
Cheibub5=Cheibub4.replace("Congo (Brazzaville, Republic of Congo)", "Republic of the Congo").replace("Brunei Darussalam", "Brunei")
Cheibub5.loc[(Cheibub5['ctryname'] == "Serbia-Montenegro") & (Cheibub5['year'] > 1991), 'ctryname'] = 'Yugoslavia'
Cheibub5.loc[(Cheibub5['ctryname'] == "Yugoslavia") & (Cheibub5['year'] > 2002), 'ctryname'] = 'Serbia-Montenegro'
Cheibub5.loc[(Cheibub5['ctryname'] == "Serbia-Montenegro") & (Cheibub5['year'] > 2006), 'ctryname'] = 'Serbia'
Cheibub5.loc[(Cheibub5['regime'] == 0), 'regime' ] = 6
Cheibub6=Cheibub5.rename(columns={'ctryname': 'Country'})

#save a dataframe to a csv with only the columns we care about
Cheibubfinal = pd.DataFrame(Cheibub6, columns = ['Country', 'year', 'regime', 'democracy', 'agereg', 'agedem'])
Cheibubfinal.to_csv('Cheibub.csv', index=False)
