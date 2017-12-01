#!/usr/bin/env python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import statsmodels.api as sm
import statsmodels.formula.api as smf
import statsmodels as sms

df = pd.read_csv('CheibubStart.csv')


ax = sns.regplot(x='agereg', y="count", data=df, lowess = True,
            scatter_kws = {"alpha" : 0.009, "color" : "blue"}, line_kws = {"color" : "gray"});
ax.set(xlabel='Regime Age', ylabel='Total number of attacks by country', title = "Regression Plot - Terrorist Attacks and Age of Regime")

axi = sns.regplot(x='agereg', y="count", data=df, lowess = True,
            scatter_kws = {"alpha" : 0.009, "color" : "blue"}, line_kws = {"color" : "gray"});
axi.set(xlabel='Age of Democracy', ylabel='Total number of attacks by country', title = "Regression Plot - Terrorist Attacks and Age of Democracy")

plt.savefig('figure14.png', bbox_inches='tight')
