import statsmodels.api as sm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv
from shapely.geometry import Point

#open csv files
df = pd.read_csv('CheibubStart.csv').dropna()
oecdg8 = pd.read_csv('2008_g8_oecd.csv')
#created a new dataframe of 2008 values
lastyear = df[df['year'] == 2008].dropna()
#merged files
g8OECD2008=pd.merge(lastyear, oecdg8, how = 'outer').dropna(subset=['year']).fillna(0)
#converted OECD variable to an integer
g8OECD2008['OECD']=g8OECD2008['OECD'].astype(int)
#created percentage values
percentG8=g8OECD2008['G8'].sum()/g8OECD2008['G8'].agg({'count'})
percentnotG8=(g8OECD2008['G8'].sum()/g8OECD2008['G8'].agg({'count'})-1)*(-1)
#created new dataframes and appended
g8=pd.DataFrame(percentnotG8)
notg8=pd.DataFrame(percentG8)
sizes=g8.append(notg8, ignore_index=True)

#created a pie chart
labels = ['Rest of the World', 'G8']
colors = ['gold', 'yellowgreen']
explode = (0.3, 0)

#plotted pie chart
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')

#set title
plt.title('Comparing the occurrence of terror attacks in G8 countries and the Rest of the World', bbox={'facecolor':'0.9', 'pad':5})

#save figure
plt.savefig('figure12.png', bbox_inches='tight')
