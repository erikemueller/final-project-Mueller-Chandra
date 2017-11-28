import pandas as pd
import numpy as np
import csv
#import csvs
Cheibub=pd.read_csv('Cheibub.csv')
START=pd.read_csv('STARTfinal.csv')
#merge
chebuibStart = pd.merge(START, Cheibub, how='outer')
#fill na values with new numeric values
#HOW DO I DO THIS
chebuibStart["regime"].fillna(chebuibStart["regime"].fillna(0), inplace=True)
#add text for regime type
chebuibStart.loc[(chebuibStart['regime'] == 0.0), 'regimetxt'] = 'Unknown/Other type or Occupied Territory'
chebuibStart.loc[(chebuibStart['regime'] == 1.0), 'regimetxt'] = 'Mixed democracy'
chebuibStart.loc[(chebuibStart['regime'] == 2.0), 'regimetxt'] = 'Presidential democracy'
chebuibStart.loc[(chebuibStart['regime'] == 3.0), 'regimetxt'] = 'Civilian dictatorship'
chebuibStart.loc[(chebuibStart['regime'] == 4.0), 'regimetxt'] = 'Military dictatorship'
chebuibStart.loc[(chebuibStart['regime'] == 5.0), 'regimetxt'] = 'Royal dictatorship'
chebuibStart.loc[(chebuibStart['regime'] == 6.0), 'regimetxt'] = 'Parliamentary democracy'

#save dataframe to csv
chebuibStart.to_csv('chebuibStart.csv', index=False)
