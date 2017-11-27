# Final Project for Meghana Chandra and Erik Mueller
For this project, we have selected four datasets and merged them together.
These datasets include:
1. The University of Maryland - College Park's Global Terrorism Database dataset (joining to parts, the almost complete set and the indpenendent values for 1993).
2. Cheibub, Gandhi, and Vreeland's Democracy and Dictatorship dataset.
3. The Gapminder dataset for country area by year.
4. The Gapminder dataset for country population by year.

The merged version of these four datasets selects for the years extending from 1970 - 2008. This selection is made due to it being the years for which each dataset has values. An issue emerged for North and South Vietnam, in that the Gapminder datasets do not seem to include them individually.

## Getting the data
1. To begin, the file *data1.py* downloads the massive GTD dataset and merges it with the missing values for 1993. This merged set is then cleaned and converted to a csv named *STARTfinal.csv*
2. This is followed up by *data2.py* which downloads Cheibub, et al's data set from Cheibub's website. This dataset it then cleaned and then the necessary values are converted to a csv named *Cheibub.csv*
3. *data3.py* merges the two csvs produced in the earlier two sets of codes and writes the output to a csv named *cheibubStart*
4. *data4.py* imports the gapminder datasets, cleans them, and merges them together. These will be used in a later analysis. The output of this code is converted to the csv file named *gap.csv*

## Generating the Figures

1. Running *figure1.py* will produce *top10countries.pdf* which is a bar plot of total number of attacks that have occurred in the ten countries that have received the highest total number of terror attacks in the years from 1970 to 2008. These are then separated out in accordance with that country's regime type and the total number of attacks that occurred in it as that regime type. Some countries have only had one type of regime during these years, but others have had two or three.
2. *figure2.py* will produce *regimeattacktype.pdf*, this plot shows the total number of attacks experienced by specific regime types over the years examined.
3. *figure3.py* generates *Plot of total attacks by Regime type.pdf* which is a similar plot to the one above, but does not separate out by attack type. 
4. *figure4.py* produces *regimeattacktype2008.pdf*. This plot shows the total number of attacks experienced by specific regime types in 2008.
5. *figure5.py* produces *country2008attacktype.pdf*. This plot shows the total number of attacks experienced by the ten countries that experienced the most attacks in 2008 and are then broken down by the type of attack.
6. *figure6.py* produces *toptencountry2008.pdf*. This plot shows the total number of attacks experienced by the ten countries that experienced the most attacks in 2008.
7. *figure7.py* produces *top10ratepermillion2008.pdf*. This produces the rate of attacks per one million people in all the countries and territories that exist in the original STARTfinal file in relation to the population listed for 2008 in the gapminder dataset.  

## Generating maps
To generate the maps associated with this project, run the file *maps.py* after all the previous code has been run or the files associated with the previous programs are present. The maps produced are:
1. *1970to2008attacktype.pdf*: This is a map of every attack that occurred from 1970 to 2008 and is color coded by attack type. It is over a map of the world. This map uses world borders as they were in 2008.
2. *1970to2008regimeattack.pdf*: This is a map of every attack that occurred from 1970 to 2008 and is color coded by regime type. It is over a map of the world. This map uses world borders as they were in 2008.
3. *2008attacktype.pdf*: This is a map of every attack that occurred in 2008 and is color coded by attack type. It is over a map of the world. This map uses world borders as they were in 2008.
4. *2008regimeattack.pdf*: This is a map of every attack that occurred in 2008 and is color coded by regime type of the nation in which it occurred. It is over a map of the world. This map uses world borders as they were in 2008.