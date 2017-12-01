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

#open csv file
df = pd.read_csv('CheibubStart.csv')

#create a factorplot of democracy and count
ax = sns.factorplot(x='democracy', y="count", data=df, kind="box", palette="muted")

#set title and labels
ax.set(xlabel='Democracy', ylabel='Total number of attacks by country', title = "Distribution of Terrorist Attacks in Democracies")

#set xticks
plt.xticks(range(2), ('Not a Democracy', 'Democracy'), rotation=30)

#save figure
plt.savefig('figure11.png', bbox_inches='tight')
