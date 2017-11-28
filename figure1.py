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

df = pd.read_csv('CheibubStart.csv').dropna()
lastyear = df[df['year'] == 2008]

sns.set(style="white")
ax = sns.countplot(x="Country", hue="regimetxt", data=df, order=df.Country.value_counts().iloc[:10].index)
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
ax.set(xlabel='Country', ylabel='Total number of attacks', title = "Total attacks in top 10 hit countries from 1970 to 2008")
ax.set_position([0.2,0.2,1.5,0.8])
leg = ax.legend(loc = 'center left', bbox_to_anchor = (1.0, 0.5))
plt.savefig('top10countries.pdf', bbox_inches='tight')
