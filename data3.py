import pandas as pd
import numpy as np
import csv
#import csvs
Cheibub=pd.read_csv('Cheibub.csv')
START=pd.read_csv('STARTfinal.csv')
#merge
CheibubStart = pd.merge(START, Cheibub, how='outer')
#fill na values with new numeric values


CheibubStart["regime"].fillna(CheibubStart["regime"].fillna(0), inplace=True)
CheibubStart = CheibubStart[CheibubStart['year'] <= 2008].dropna()
#add text for regime type
CheibubStart.loc[(CheibubStart['regime'] == 0.0), 'regimetxt'] = 'Unknown/Other type or Occupied Territory'
CheibubStart.loc[(CheibubStart['regime'] == 1.0), 'regimetxt'] = 'Mixed democracy'
CheibubStart.loc[(CheibubStart['regime'] == 2.0), 'regimetxt'] = 'Presidential democracy'
CheibubStart.loc[(CheibubStart['regime'] == 3.0), 'regimetxt'] = 'Civilian dictatorship'
CheibubStart.loc[(CheibubStart['regime'] == 4.0), 'regimetxt'] = 'Military dictatorship'
CheibubStart.loc[(CheibubStart['regime'] == 5.0), 'regimetxt'] = 'Royal dictatorship'
CheibubStart.loc[(CheibubStart['regime'] == 6.0), 'regimetxt'] = 'Parliamentary democracy'

#save dataframe to csv
CheibubStart.to_csv('CheibubStart.csv', index=False)
