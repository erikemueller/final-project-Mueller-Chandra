#!/usr/bin/env python

import statsmodels.api as sm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv
from shapely.geometry import Point
import geopandas as gpd
from geopandas import GeoSeries, GeoDataFrame
#import data
df = pd.read_csv('CheibubStart.csv')
#drop values that have empty fames but for events with lat long for countries w/ unknown regime type
df=df.drop('agereg', axis = 1).drop('democracy', axis = 1).drop('agedem', axis = 1)
#drop the na values so that things plot
df=df.dropna()
#import shapefile of world in 2008
fp = "world/TM_WORLD_BORDERS_SIMPL-0.3.shp"
data = gpd.read_file(fp)
#select only values from 2008
lastyear = df[df['year'] == 2008]
fp = "world/TM_WORLD_BORDERS_SIMPL-0.3.shp"
data = gpd.read_file(fp)
#set up map
geometry = [Point(xy) for xy in zip(lastyear['longitude'], lastyear['latitude'])]
lastyear.drop(['longitude', 'latitude'], axis=1)
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
gdf = GeoDataFrame(lastyear, crs=data, geometry=geometry)
#map
sns.set(style="white")
ax=gdf.plot(marker='*', column = 'attacktype1_txt', markersize=5, figsize=(30, 30), legend=True)
data.plot(ax = ax, facecolor="none", edgecolor='grey')
leg = ax.legend(loc = 'center left', bbox_to_anchor = (1.0, 0.5))
plt.savefig('map1.png', bbox_inches='tight')
#second map
sns.set(style="white")
ax=gdf.plot(marker='*', column = 'regimetxt', markersize=5, figsize=(30, 30), legend=True)
data.plot(ax = ax, facecolor="none", edgecolor='grey')
leg = ax.legend(loc = 'center left', bbox_to_anchor = (1.0, 0.5))
plt.savefig('map2.png', bbox_inches='tight')
