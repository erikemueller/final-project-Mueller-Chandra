#!/usr/bin/env python

#import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import statsmodels.api as sm
import statsmodels.formula.api as smf
import statsmodels as sms

#open csvs and merge
df = pd.read_csv('CheibubStart.csv')
gap = pd.read_csv('gap.csv')
gapStart=pd.merge(df, gap)

#regression using statsmodels
ols = smf.ols("count ~ C(democracy) + agedem + np.log(Population)", data = gapStart)
model = ols.fit()

#print regression
print (model.summary())
