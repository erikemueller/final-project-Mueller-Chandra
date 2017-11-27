import pandas as pd
import numpy as np
import csv

Gapminder = pd.read_excel('Gapminder.xlsx')
Gapminder1=Gapminder.rename(columns={'Total population': 'Country'})
Gapminder2 = pd.melt(Gapminder1, id_vars=["Country"], var_name="year", value_name="Population")
GapminderClean=Gapminder2.replace("Antigua and Barbuda", "Antigua & Barbuda").replace("Bosnia and Herzegovina", "Bosnia-Herzegovina").replace("Kyrgyz Republic", "Kyrgyzstan").replace("Lao", "Laos").replace("USSR", "Soviet Union").replace('South Yemen (former)', 'South Yemen').replace('Serbia and Montenegro', 'Serbia-Montenegro').replace('North Yemen (former)', 'North Yemen').replace('Timor-Leste', 'East Timor')

Gapminderarea=pd.read_excel('Gapminderarea.xlsx', header=0).dropna(axis=1, how='all')
Gapminderarea1=Gapminderarea.rename(columns={'Surface area (sq. km)': 'Country'})
Gapminderarea2 = pd.melt(Gapminderarea1, id_vars=["Country"], var_name="year", value_name="area")
Gapminderarea2['year'] = Gapminderarea2['year'].astype(int)
GapminderareaClean=Gapminderarea2.replace("Antigua and Barbuda", "Antigua & Barbuda").replace("Bosnia and Herzegovina", "Bosnia-Herzegovina").replace("Kyrgyz Republic", "Kyrgyzstan").replace("Lao", "Laos").replace("USSR", "Soviet Union").replace('South Yemen (former)', 'South Yemen').replace('Serbia and Montenegro', 'Serbia-Montenegro').replace('North Yemen (former)', 'North Yemen').replace('Timor-Leste', 'East Timor')

gap=pd.merge(GapminderClean, GapminderareaClean)

gap.to_csv('gap.csv', index=False)