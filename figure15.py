#!/usr/bin/env python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import statsmodels.api as sm
import statsmodels.formula.api as smf
import statsmodels as sms

#open csv file
df = pd.read_csv('CheibubStart.csv')

#create regression plot of count of terrorist attacks and age of Democracy

ax = sns.regplot(x='agedem', y="count", data=df, lowess = True,
            scatter_kws = {"alpha" : 0.009, "color" : "blue"}, line_kws = {"color" : "gray"});

#set labels and title
ax.set(xlabel='Age of Democracy', ylabel='Total number of attacks by country', title = "Regression Plot - Terrorist Attacks and Age of Democracy")

#save figure
plt.savefig('figure15.png', bbox_inches='tight')
