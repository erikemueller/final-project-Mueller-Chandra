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

groupyear=df.groupby([df['year'], df['Country']]).agg({'count'})
groupyear.reset_index(level=1, inplace=True)
groupyear.reset_index(level=0, inplace=True)
groupyear=groupyear[groupyear.columns[0:3]]
groupyear=groupyear.rename(columns={'region_txt': 'count'})
groupyear.columns = groupyear.columns.droplevel(-1)
gapwork=gap[(gap['year'] <= 2008) & (gap['year'] >= 1970)]
df1 = df[['Country','regimetxt']]
df2=df1.drop_duplicates(keep='first')


countedCount=pd.merge(gapwork, groupyear, how='outer').dropna(subset=['Population'])
countedCount=pd.merge(countedCount, df2)
countedCount['rate'] = np.where(countedCount['count'] < 1, countedCount['Population'], countedCount['count']/(countedCount['Population']/1000000))
countedCount=countedCount.fillna(0)
print(countedCount)
