import pandas as pd
import numpy as np
import csv
#import csvs
Cheibub=pd.read_csv('Cheibub.csv')
START=pd.read_csv('STARTfinal.csv')
#merge
chebuibStart = pd.merge(START, Cheibub)
#add text for regime type
chebuibStart.loc[:,'regimetxt'] = chebuibStart['regime']
chebuibStart.loc[(chebuibStart['regimetxt'] == 0.0), 'regimetxt'] = 'Parliamentary democracy'
chebuibStart.loc[(chebuibStart['regimetxt'] == 1.0), 'regimetxt'] = 'Mixed democracy'
chebuibStart.loc[(chebuibStart['regimetxt'] == 2.0), 'regimetxt'] = 'Presidential democracy'
chebuibStart.loc[(chebuibStart['regimetxt'] == 3.0), 'regimetxt'] = 'Civilian dictatorship'
chebuibStart.loc[(chebuibStart['regimetxt'] == 4.0), 'regimetxt'] = 'Military dictatorship'
chebuibStart.loc[(chebuibStart['regimetxt'] == 5.0), 'regimetxt'] = 'Royal dictatorship'

#save dataframe to csv
chebuibStart.to_csv('chebuibStart.csv', index=False)