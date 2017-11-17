import pandas as pd
import csv

Gapminder = pd.read_excel('Gapminder.xlsx')
Gapminder1=Gapminder.rename(columns={'Total population': 'Country'})
Gapminder2 = pd.melt(Gapminder1, id_vars=["Country"], var_name="year", value_name="Population")
GapminderClean=Gapminder2.replace("Antigua and Barbuda", "Antigua & Barbuda").replace("Bosnia and Herzegovina", "Bosnia-Herzegovina").replace("Kyrgyz Republic", "Kyrgyzstan").replace("Lao", "Laos").replace("USSR", "Soviet Union").replace('South Yemen (former)', 'South Yemen').replace('Serbia and Montenegro', 'Serbia-Montenegro').replace('North Yemen (former)', 'North Yemen')

Gapminderarea=pd.read_excel('Gapminderarea.xlsx', header=0).dropna(axis=1, how='all')
Gapminderarea1=Gapminderarea.rename(columns={'Surface area (sq. km)': 'Country'})
Gapminderarea2 = pd.melt(Gapminderarea1, id_vars=["Country"], var_name="year", value_name="area")
Gapminderarea2['year'] = Gapminderarea2['year'].astype(int)
GapminderareaClean=Gapminderarea2.replace("Antigua and Barbuda", "Antigua & Barbuda").replace("Bosnia and Herzegovina", "Bosnia-Herzegovina").replace("Kyrgyz Republic", "Kyrgyzstan").replace("Lao", "Laos").replace("USSR", "Soviet Union").replace('South Yemen (former)', 'South Yemen').replace('Serbia and Montenegro', 'Serbia-Montenegro').replace('North Yemen (former)', 'North Yemen')

gap=pd.merge(GapminderClean, GapminderareaClean)

Chebuib=pd.read_excel("Chebuib.xls")

Chebuib1=Chebuib.replace("United States of America", "United States").replace("Germany, East", "East Germany").replace("Germany, West", "West Germany")
Chebuib2=Chebuib1.replace("Democratic Republic of the Congo (Zaire, Congo-Kinshasha)", "Democratic Republic of the Congo").replace("Viet Nam", "Vietnam").replace("Vietnam, South", "South Vietnam").replace("Vietnam, North", "North Vietnam")
Chebuib3=Chebuib2.replace("Yemen PDR (South)", "South Yemen").replace("Yemen Arab Republic", "North Yemen").replace("Serbia and Montenegro", "Serbia-Montenegro").replace("Russian Federation", "Russia")
Chebuib4=Chebuib3.replace("Bosnia and Herzegovina", "Bosnia-Herzegovina").replace("U.S.S.R.", "Soviet Union").replace("Libyan Arab Jamahiriya", "Libya")
Chebuib5=Chebuib4.replace("Congo (Brazzaville, Republic of Congo)", "Republic of the Congo").replace("Brunei Darussalam", "Brunei")

START=pd.read_excel('START.xlsx')

START1993=pd.read_excel('START1993.xlsx')

STARTclean=START.append(START1993, ignore_index=True)

START1=STARTclean.replace("West Germany (FRG)", "West Germany").replace("East Germany (GDR)", "East Germany").replace("Zaire", "Democratic Republic of the Congo")
START2=START1.replace("Rhodesia", "Zimbabwe").replace("French Polynesia", "France").replace("French Guiana", "France").replace("Guadeloupe", "France").replace("Martinique", "France").replace("New Caledonia", "France").replace("Wallis and Futuna", "France")
START3=START2.replace("Macau", "Portugal").replace("International", "Yemen").replace("Slovak Republic", "Slovakia").replace("Ivory Coast", "Cote d'Ivoire").replace("People's Republic of the Congo", "Republic of the Congo")
START4=START3.replace("Antigua and Barbuda", "Antigua & Barbuda")

START4.loc[(START4['country_txt'] == "Namibia") & (START4['iyear'] < 1990), 'country_txt'] = 'South Africa'
START4.loc[(START4['country_txt'] == "Soviet Union") & (START4['iyear'] == 1990), 'country_txt'] = 'Russia'
START4.loc[(START4['country_txt'] == "Hong Kong") & (START4['iyear'] < 1997), 'country_txt'] = 'United Kingdom'
START4.loc[(START4['country_txt'] == "Hong Kong") & (START4['iyear'] > 1997), 'country_txt'] = 'China'
START4.loc[(START4['country_txt'] == "West Germany") & (START4['iyear'] == 1990), 'country_txt'] = 'Germany'
START4.loc[(START4['country_txt'] == "East Germany") & (START4['iyear'] == 1990), 'country_txt'] = 'Germany'
START4.loc[(START4['country_txt'] == "East Timor") & (START4['iyear'] < 2002), 'country_txt'] = 'Indonesia'
START4.loc[(START4['country_txt'] == "Serbia-Montenegro") & (START4['iyear'] > 2006), 'country_txt'] = 'Serbia'
START4.loc[(START4['country_txt'] == "Montenegro") & (START4['iyear'] == 2001), 'country_txt'] = 'Yugoslavia'
START4.loc[(START4['country_txt'] == "Belize") & (START4['iyear'] == 1980), 'country_txt'] = 'United Kingdom'
Chebuib5.loc[(Chebuib5['ctryname'] == "Serbia-Montenegro") & (Chebuib5['year'] > 1991), 'ctryname'] = 'Yugoslavia'
Chebuib5.loc[(Chebuib5['ctryname'] == "Yugoslavia") & (Chebuib5['year'] > 2002), 'ctryname'] = 'Serbia-Montenegro'
Chebuib5.loc[(Chebuib5['ctryname'] == "Serbia-Montenegro") & (Chebuib5['year'] > 2006), 'ctryname'] = 'Serbia'
START5 = START4.rename(columns={'country_txt': 'Country', 'iyear': 'year'})
Chebuib6=Chebuib5.rename(columns={'ctryname': 'Country'})

chebuibStart = pd.merge(START5, Chebuib6)
gapStart=pd.merge(chebuibStart, gap).dropna(axis=1, how='all').drop('country', axis =1).drop('extended', axis =1).drop('approxdate', axis =1).drop('resolution', axis =1)
