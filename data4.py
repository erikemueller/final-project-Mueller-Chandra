#!/usr/bin/env python

import pandas as pd
import numpy as np
import csv
#import csv
Gapminder = pd.read_excel('Gapminder.xlsx')
#rename headers
Gapminder1=Gapminder.rename(columns={'Total population': 'Country'})
#turn year headers into a column
Gapminder2 = pd.melt(Gapminder1, id_vars=["Country"], var_name="year", value_name="Population")
#rename values so they merge later
gap=Gapminder2.replace("Antigua and Barbuda", "Antigua & Barbuda").replace("Bosnia and Herzegovina", "Bosnia-Herzegovina").replace("Kyrgyz Republic", "Kyrgyzstan").replace("Lao", "Laos").replace("USSR", "Soviet Union").replace('South Yemen (former)', 'South Yemen').replace('Serbia and Montenegro', 'Serbia-Montenegro').replace('North Yemen (former)', 'North Yemen').replace('Timor-Leste', 'East Timor')


gap.to_csv('gap.csv', index=False)
