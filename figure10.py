#!/usr/bin/env python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import statsmodels.api as sm
import statsmodels.formula.api as smf
import statsmodels as sms
import matplotlib.pyplot as plt
from matplotlib.ticker import *

#open csv
df = pd.read_csv('CheibubStart.csv')

#create factorplot of regime and count
ax = sns.factorplot(x='regime', y="count", data=df, kind="box", palette="muted", size=6, aspect=2)
#set labels and title
ax.set(xlabel='Regime(Type)', ylabel='Total number of attacks by country', title = "Distribution of Terrorist Attacks by Regime Type")
#change tick labels to reflect regime names
plt.xticks(range(7), ('Unknown Regime/Occupied Territory','Mixed Democracy', 'Presidential Democracy','Civilian Dictatorship', 'Military Dictatorship', 'Royal Dictatorship', 'Parliamentary Democracy'), rotation=90) #would be range(3xx), List_of_city_names, rotation=90
#save figure as png file
plt.savefig('figure10.png', bbox_inches='tight')
