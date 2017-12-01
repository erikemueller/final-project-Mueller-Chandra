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

df = pd.read_csv('CheibubStart.csv')

ax = sns.factorplot(x='democracy', y="count", data=df, kind="box", palette="muted")

ax.set(xlabel='Democracy', ylabel='Total number of attacks by country', title = "Distribution of Terrorist Attacks in Democracies")

plt.xticks(range(6), ('Not a Democracy', 'Democracy'), rotation=30)

plt.savefig('figure11.png', bbox_inches='tight')
