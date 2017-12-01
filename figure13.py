import statsmodels.api as sm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv
from shapely.geometry import Point

#opened csv files
df = pd.read_csv('CheibubStart.csv').dropna()
oecdg8 = pd.read_csv('2008_g8_oecd.csv')

#created a dataframe of 2008 values
lastyear = df[df['year'] == 2008].dropna()

#merge dataframes
g8OECD2008=pd.merge(lastyear, oecdg8, how = 'outer').dropna(subset=['year']).fillna(0)

#convert to integer
g8OECD2008['OECD']=g8OECD2008['OECD'].astype(int)

#create percentage values
percentOECD=g8OECD2008['OECD'].sum()/g8OECD2008['OECD'].agg({'count'})
percentnotOECD=(g8OECD2008['OECD'].sum()/g8OECD2008['OECD'].agg({'count'})-1)*(-1)

#create dataframes with percentage values and append
OECD=pd.DataFrame(percentOECD)
notOECD=pd.DataFrame(percentnotOECD)
yall=OECD.append(notOECD, ignore_index=True)

#create pie chart
labels = ['OECD', 'Rest of the World']
colors = ['blue', 'yellow']
explode = (0.3, 0)

#plot pie chart
plt.pie(yall, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')

#set title
plt.title('Comparing the occurrence of terror attacks in OECD countries and the Rest of the World', bbox={'facecolor':'0.9', 'pad':5})

#save figure
plt.savefig('figure13.png', bbox_inches='tight')
