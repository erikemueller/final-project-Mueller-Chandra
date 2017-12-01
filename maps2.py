import statsmodels.api as sm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv
from shapely.geometry import Point
import geopandas as gpd
from geopandas import GeoSeries, GeoDataFrame

df = pd.read_csv('CheibubStart.csv')
df=df.drop('agereg', axis = 1).drop('democracy', axis = 1).drop('agedem', axis = 1)
df=df.dropna()

fp = "world/TM_WORLD_BORDERS_SIMPL-0.3.shp"
data = gpd.read_file(fp)

geometry = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]
df.drop(['longitude', 'latitude'], axis=1)
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
gdf = GeoDataFrame(df, crs=data, geometry=geometry)

sns.set(style="white")
ax=gdf.plot(marker='*', cmap = "nipy_spectral", column = 'attacktype1_txt', markersize=5, figsize=(30, 30), legend=True)
data.plot(ax = ax, facecolor="none", edgecolor='grey')
leg = ax.legend(loc = 'center left', bbox_to_anchor = (1.0, 0.5))
plt.savefig('map3.png', bbox_inches='tight')

sns.set(style="white")
ax=gdf.plot(marker='*', cmap = "nipy_spectral", column = 'regimetxt', markersize=5, figsize=(30, 30), legend=True)
data.plot(ax = ax,  facecolor="none", edgecolor='grey')
leg = ax.legend(loc = 'center left', bbox_to_anchor = (1.0, 0.5))
plt.savefig('map4.png', bbox_inches='tight')
