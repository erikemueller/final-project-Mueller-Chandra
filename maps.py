import statsmodels.api as sm 
import pandas as pd
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt 
plt.rc("font", size=14)
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
import seaborn as sns
import csv
from shapely.geometry import Point
import geopandas as gpd
from geopandas import GeoSeries, GeoDataFrame

df = pd.read_csv('chebuibStart.csv').dropna()

fp = "world/TM_WORLD_BORDERS_SIMPL-0.3.shp"
data = gpd.read_file(fp)

lastyear = df[df['year'] == 2008]
fp = "world/TM_WORLD_BORDERS_SIMPL-0.3.shp"
data = gpd.read_file(fp)

geometry = [Point(xy) for xy in zip(lastyear['longitude'], lastyear['latitude'])]
lastyear.drop(['longitude', 'latitude'], axis=1)
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
gdf = GeoDataFrame(lastyear, crs=data, geometry=geometry)

sns.set(style="white")
data.plot(ax=gdf.plot(marker='*', column = 'attacktype1_txt', markersize=5, figsize=(30, 30), legend=True),  facecolor="none", edgecolor='grey')
plt.savefig('2008attacktype.pdf', bbox_inches='tight')


sns.set(style="white")
data.plot(ax=gdf.plot(marker='*', column = 'regimetxt', markersize=5, figsize=(30, 30), legend=True),  facecolor="none", edgecolor='grey')
plt.savefig('2008regimeattack.pdf', bbox_inches='tight')

geometry = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]
df.drop(['longitude', 'latitude'], axis=1)
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
gdf = GeoDataFrame(df, crs=data, geometry=geometry)

sns.set(style="white")
data.plot(ax=gdf.plot(marker='*', column = 'attacktype1_txt', markersize=5, figsize=(30, 30), legend=True),  facecolor="none", edgecolor='grey')
plt.savefig('1970to2008attacktype.pdf', bbox_inches='tight')

sns.set(style="white")
data.plot(ax=gdf.plot(marker='*', column = 'regimetxt', markersize=5, figsize=(30, 30), legend=True),  facecolor="none", edgecolor='grey')
plt.savefig('1970to2008regimeattack.pdf', bbox_inches='tight')