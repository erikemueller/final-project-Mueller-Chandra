# Final Project for Meghana Chandra and Erik Mueller
 ## The Question 
This project is an attempt to understand the interaction betweeen governmental regimes and terrorist attacks. It was motivated by a need to explore the relationship between the system of government and terrorist attacks - in relation to targets as well as perpetrators. We wanted to examine if increased representation, and the age of the prevalent governmental regime influenced the number of terrorist attacks. We begin by exploring the data with and without normalizations using population. Furthermore, we use maps to understand the distribution of terrorist attacks. We finally investigate to what extent regimes and the age of the prevalent regime influences the occurence of terrorist attacks. 
 
 ## Literature Review 
 
 Regimes are understood in political science literature as a "unique set of procedural institutions -formal or informal rules -that determine political access and are accepted by major political actors" (Gasiorowski 1996; Kitschelt 1992; Munck 1996). It has been argued that democracies allow for greater representation, thereby allowing for criticism of the regime to be expressed through peaceful and legal means (Eyerman 1998), however, it hasa been said that increased control in autocratic regimes makes terrorism less likely, and  more likely in democracies (Gandhi 2008). 

## The Data 
For this project, we have selected three datasets and merged them together.

These datasets include:
1. The University of Maryland - College Park's Global Terrorism Database dataset (joining to parts, the almost complete set and the indpenendent values for 1993).
2. Cheibub, Gandhi, and Vreeland's Democracy and Dictatorship dataset.
3. The Gapminder dataset for country population by year.

The merged version of these four datasets selects for the years extending from 1970 - 2008. This selection is made due to it being the years for which each dataset has values. An issue emerged for North and South Vietnam, in that the Gapminder datasets do not seem to include them individually.

## Getting the data
1. To begin, the file *data1.py* downloads the massive GTD dataset and merges it with the missing values for 1993. This merged set is then cleaned and converted to a csv named *STARTfinal.csv*
2. This is followed up by *data2.py* which downloads Cheibub, et al's data set from Cheibub's website. This dataset it then cleaned and then the necessary values are converted to a csv named *Cheibub.csv*
3. *data3.py* merges the two csvs produced in the earlier two sets of codes and writes the output to a csv named *cheibubStart*
4. *data4.py* imports the gapminder datasets, cleans them, and merges them together. These will be used in a later analysis. The output of this code is converted to the csv file named *gap.csv*

## Generating the Figures

1. Running *figure1.py* will produce *top10countries.pdf* which is a bar plot of total number of attacks that have occurred in the ten countries that have received the highest total number of terror attacks in the years from 1970 to 2008. These are then separated out in accordance with that country's regime type and the total number of attacks that occurred in it as that regime type. Some countries have only had one type of regime during these years, but others have had two or three.
![Figure 1](top10countries.pdf "Figure 1") can be found here.
2. *figure2.py* will produce *regimeattacktype.pdf*, this plot shows the total number of attacks experienced by specific regime types over the years examined. ![Figure 2](regimeattacktype.pdf "Figure 2") can be found here.
3. *figure3.py* generates *PlotoftotalattacksbyRegimetype.pdf* which is a similar plot to the one above, but does not separate out by attack type. ![Figure 3](PlotoftotalattacksbyRegimetype.pdf "Figure 3") can be found here.
4. *figure4.py* produces *regimeattacktype2008.pdf*. This plot shows the total number of attacks experienced by specific regime types in 2008. ![Figure 4](regimeattacktype2008.pdf "Figure 4") can be found here.
5. *figure5.py* produces *country2008attacktype.pdf*. This plot shows the total number of attacks experienced by the ten countries that experienced the most attacks in 2008 and are then broken down by the type of attack. ![Figure 5](country2008attacktype.pdf "Figure 5") can be found here.
6. *figure6.py* produces *toptencountry2008.pdf*. This plot shows the total number of attacks experienced by the ten countries that experienced the most attacks in 2008. ![Figure 6](toptencountry2008.pdf "Figure 6") can be found here.
7. *figure7.py* produces *top10ratepermillion2008.pdf*. This produces the rate of attacks per one million people in all the countries and territories that exist in the original STARTfinal file in relation to the population listed for 2008 in the gapminder dataset.  ![Figure 7](top10ratepermillion2008.pdf "Figure 7") can be found here.

## Generating maps
To generate the maps associated with this project, run the file *maps.py* after all the previous code has been run or the files associated with the previous programs are present. The maps produced are:
1. *1970to2008attacktype.pdf*: This is a map of every attack that occurred from 1970 to 2008 and is color coded by attack type. It is over a map of the world. This map uses world borders as they were in 2008.
2. *1970to2008regimeattack.pdf*: This is a map of every attack that occurred from 1970 to 2008 and is color coded by regime type. It is over a map of the world. This map uses world borders as they were in 2008.
3. *2008attacktype.pdf*: This is a map of every attack that occurred in 2008 and is color coded by attack type. It is over a map of the world. This map uses world borders as they were in 2008.
4. *2008regimeattack.pdf*: This is a map of every attack that occurred in 2008 and is color coded by regime type of the nation in which it occurred. It is over a map of the world. This map uses world borders as they were in 2008. 
## Investigating the influence of regimes on the number of terrorist attacks 
We generated factorplots of democracy and regime in relation to the count of terrorist attacks in order to examine the effect of the same on the count of attacks. We did this using *figure7.py* and *figure8.py* producing *demplot.pdf* and *regplot.pdf* which provide us with an indicator of the range of attacks, as well as the presence of outliers. The outliers indicated herein are two years in Iraq - 2007 and 2008 which does not appear to be unlikely. *figure9.py* and *figure10.py* plot the number of attacks in a particular year in a particular country against the age of that specific regime or a specific democracy, in doing so we aim to examine the interaction between the two variables. As can be seen the regression does not explain the data very well, however there does appear to be a reduction in the number of terrorist attacks, the older the regime. The regression line appears to be slightly flatter when all the regimes are considered, as opposed to only democracies. In the figure with the age of democracies, it is interesting to note that there appears to be increased terrorism in countries that have existed as democracies for 60-80 years - which is perhaps indicative of increased terrorism amongst countries that were colonized but became independent around the 1930s and 40s.