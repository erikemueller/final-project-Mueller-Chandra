import statsmodels.api as sm
import pandas as pd
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt
plt.rc("font", size=14)
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
import seaborn as sns
import csv
from shapely.geometry import Point
import collections

df = pd.read_csv('CheibubStart.csv')
gap =pd.read_csv('gap.csv')
lastyear = df[df['year'] == 2008]
df1 = lastyear[['Country','regimetxt']]
df2=df1.drop_duplicates(keep='first')

countrycount=collections.Counter(lastyear["Country"])
countryCount = pd.DataFrame.from_dict(countrycount, orient='index').reset_index()
countryCount =countryCount.rename(index=str, columns={"index": "Country", 0: "count"})

gap2008 = gap[gap['year'] == 2008]
countedCount=pd.merge(gap2008, countryCount, how='outer').dropna(subset=['Population'])
countedCount=pd.merge(countedCount, df2)
countedCount['rate'] = np.where(countedCount['count'] < 1, countedCount['Population'], countedCount['count']/(countedCount['Population']/1000000))
countedCount=countedCount.fillna(0)
top10for2008=countedCount.sort_values('rate').tail(10)

sns.set(style="white")
ax = sns.barplot(x="Country", y="rate", hue='regimetxt', data=top10for2008)
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
ax.set(xlabel='Country', ylabel='Attacks per 1 million people', title = "10 countries and territories with highest rate of attacks per 1 million people for 2008")
ax.set_position([0.2,0.2,1.5,0.8])
leg = ax.legend(loc = 'center left', bbox_to_anchor = (1.0, 0.5))
plt.savefig('figure7.png', bbox_inches='tight')
