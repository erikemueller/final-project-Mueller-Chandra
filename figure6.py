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
ax = sns.countplot(x="Country", data=lastyear, order=lastyear.Country.value_counts().iloc[:10].index)
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
ax.set(xlabel='Country', ylabel='Total number of attacks', title = "Total attacks by regime type for 2008")
ax.set_position([0.2,0.2,1.5,0.8])
leg = ax.legend(loc = 'center left', bbox_to_anchor = (1.0, 0.5))
plt.savefig('toptencountry2008.pdf', bbox_inches='tight')
