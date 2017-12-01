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

#create regression plot of number of terrorist attacks and the age of the regime
ax = sns.regplot(x='agereg', y="count", data=df, lowess = True,
            scatter_kws = {"alpha" : 0.009, "color" : "blue"}, line_kws = {"color" : "gray"});

#set labels and title
ax.set(xlabel='Regime Age', ylabel='Total number of attacks by country', title = "Regression Plot - Terrorist Attacks and Age of Regime")

#save figure
plt.savefig('figure14.png', bbox_inches='tight')
