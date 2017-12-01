# Final Project for Meghana Chandra and Erik Mueller
 ## The Question 
This project is an attempt to understand the interaction betweeen governmental regimes and terrorist attacks. It was motivated by a need to explore the relationship between the system of government and terrorist attacks - in relation to targets as well as perpetrators. We wanted to examine if increased representation, and the age of the prevalent governmental regime influenced the number of terrorist attacks. We begin by exploring the data with and without normalizations using population. Furthermore, we use maps to understand the distribution of terrorist attacks. We finally investigate to what extent regimes and the age of the prevalent regime influences the occurence of terrorist attacks. 
 
 ## Literature Review 
 
 Regimes are understood in political science literature as a "unique set of procedural institutions -formal or informal rules -that determine political access and are accepted by major political actors" (Gasiorowski 1996; Kitschelt 1992; Munck 1996). It has been argued that democracies allow for greater representation, thereby allowing for criticism of the regime to be expressed through peaceful and legal means (Eyerman 1998), however, it has also been said that increased control in autocratic regimes makes terrorism less likely, and  more likely in democracies (Gandhi 2008). 

## The Data 

For this project, we have selected three datasets and merged them together.

These datasets include:
1. The University of Maryland - College Park's Global Terrorism Database dataset (joining to parts, the almost complete set and the indpenendent values for 1993).
2. Cheibub, Gandhi, and Vreeland's Democracy and Dictatorship dataset.
3. The Gapminder dataset for country population by year.
4. There is a file labelled *2008_g8_oecd.csv* that is a list of the countries that were members of the G8 and/or OECD in 2008. This will be used in later analysis for 2008 and will be joined onto the merged CheibubStart dataset. This file was made by us. It is based on membership dates of these organizations.

There is a merged file of the Cheibub, et al dataset and the GTD dataset with all values for 1970 through 2008. Gapminder's data is left separate to avoid complications later, but a cleaned up version of this file is used in later analysis. An issue emerged for North and South Vietnam, in that the Gapminder datasets do not seem to include them individually.

## Getting the data

1. To begin, the file *data1.py* downloads the massive GTD dataset and merges it with the missing values for 1993. This merged set is then cleaned and converted to a csv named *STARTfinal.csv*
2. This is followed up by *data2.py* which downloads Cheibub, et al's data set from Cheibub's website. This dataset it then cleaned and then the necessary values are converted to a csv named *Cheibub.csv*
3. *data3.py* merges the two csvs produced in the earlier two sets of codes and writes the output to a csv named *cheibubStart*
4. *data4.py* imports the gapminder dataset, and cleans it. It will be used in a later analysis. The output of this code is converted to the csv file named *gap.csv*

## Exploring the data

To begin with we explored the data by: 

(a) trying to ascertain the countries that had the highest number of 'terrorist attacks' as defined by the Global Terrorism Database, and their regimes.

[![figure1](https://github.com/erikemueller/final-project-Mueller-Chandra/blob/master/figure1.png)](#features)

Running *figure1.py* produces *figure1.png* which is a bar plot of total number of attacks that have occurred in the ten countries that have received the highest total number of terror attacks in the years from 1970 to 2008. These are then separated out in accordance with that country's regime type and the total number of attacks that occurred in it as that regime type. Some countries have only had one type of regime during these years, but others have had two or three.

(b) plotting the distribution of attack type by regime type.

[![figure2](https://github.com/erikemueller/final-project-Mueller-Chandra/blob/master/figure2.png)](#features)

*figure2.py* produces *figure2.png*, this plot shows the total number of attacks experienced by specific regime types over the years examined. 

It was interesting to note that bombing/explosion was the most common attack type across all regimes except royal dictatorships where, understandably, assassinations appear to be the primary attack type. 

(c) comparing the total number of attacks by regime type. Although the previous figure indicated that there were consistently higher number of terrorist attacks across democracies, we wanted to see if there were more attacks in democracies regardless of attack type. 

[![figure3](https://github.com/erikemueller/final-project-Mueller-Chandra/blob/master/figure3.png)](#features)

*figure3.py* generates *figure3.png* which is a similar plot to the one above, but does not separate out by attack type. 

### Breaking down the data 

We wanted to see what the data looked like for a single year. We chose 2008 because it was the most recent year for which we had Cheibub and START data.

We began by:

(a) charting the attack type for 2008 (which is the last year for which we have data in Cheibub) across regimes. We did this in order to break down the data to see what it looks like in a given year. 


[![figure4](https://github.com/erikemueller/final-project-Mueller-Chandra/blob/master/figure4.png)](#features)

*figure4.py* produces *figure4.png*. This plot shows the total number of attacks experienced by specific regime types in 2008. 

(b) plotting the ten countries with the highest number of terrorist attacks in 2008. 

[![figure5](https://github.com/erikemueller/final-project-Mueller-Chandra/blob/master/figure5.png)](#features)

*figure5.py* produces *figure5.png*. This plot shows the total number of attacks experienced by the ten countries that experienced the most attacks in 2008 and are then broken down by the type of attack. 

(c) plotting the total number of attacks by regime type in 2008.

[![figure6](https://github.com/erikemueller/final-project-Mueller-Chandra/blob/master/figure6.png)](#features)

*figure6.py* produces *figure6.png*. This plot shows the total number of attacks experienced by the ten countries that experienced the most attacks in 2008. 

We then attempted to normalize the data by population:

[![figure7](https://github.com/erikemueller/final-project-Mueller-Chandra/blob/master/figure7.png)](#features)

*figure7.py* produces *figure7.png*. This produces the rate of attacks per one million people in all the countries and territories that exist in the original STARTfinal file in relation to the population listed for 2008 in the gapminder dataset.  

In order to see what attack type is most common and which countries were the most hit (regardless of regime type), we created *figure8.png* using *figure8.py*; and *figure9.png* using *figure9.py*

[![figure9](https://github.com/erikemueller/final-project-Mueller-Chandra/blob/master/figure9.png)](#features)

## Generating maps

We generates maps associated with this project to get a pictoral representation of attacks across the world

Note: Run the file *maps.py* after all the previous code has been run or the files associated with the previous programs are present. 

The maps produced are:

1. *map1.png*: This is a map of every attack that occurred in 2008 and is color coded by attack type. It is over a map of the world. This map uses world borders as they were in 2008.

[![map1](https://github.com/erikemueller/final-project-Mueller-Chandra/blob/master/map1.png)](#features)

2. *map2.png*:This is a map of every attack that occurred in 2008 and is color coded by regime type of the nation in which it occurred. It is over a map of the world. This map uses world borders as they were in 2008. 

[![map2](https://github.com/erikemueller/final-project-Mueller-Chandra/blob/master/map2.png)](#features)

3. *map3.png*: This is a map of every attack that occurred from 1970 to 2008 and is color coded by attack type. It is over a map of the world. This map uses world borders as they were in 2008.

[![map3](https://github.com/erikemueller/final-project-Mueller-Chandra/blob/master/map3.png)](#features)

4. *map4.png*: This is a map of every attack that occurred from 1970 to 2008 and is color coded by regime type. It is over a map of the world. This map uses world borders as they were in 2008.

[![map4](https://github.com/erikemueller/final-project-Mueller-Chandra/blob/master/map4.png)](#features)

## Investigating the influence of regimes on the number of terrorist attacks 

We generated factorplots of democracy and regime in relation to the count of terrorist attacks in order to examine the effect of the same on the count of attacks. 

We did this using *figure10.py* and *figure11.py* producing *figure10.png* and *figure11.png* which provide us with an indicator of the range of attacks, as well as the presence of outliers in relation to all regimes, and in relation to democracies. 

[![figure10](https://github.com/erikemueller/final-project-Mueller-Chandra/blob/master/figure10.png)](#features)


[![figure11](https://github.com/erikemueller/final-project-Mueller-Chandra/blob/master/figure11.png)](#features)


The outliers indicated in Figure10 under Cilvian Dictatorship are two years in Iraq - 2007 and 2008; and under Parliamentary Democracy the ouliers are Pakistan in 1995 and 2008, and India in 2008.

*figure12.py* and *figure13.py* plot the distribution of attacks with specific reference to G8 and OECD countries, comparing the number of attacks in each of them, with the total number of attacks in the rest of the world.

[![figure12](https://github.com/erikemueller/final-project-Mueller-Chandra/blob/master/figure12.png)](#features)

[![figure13](https://github.com/erikemueller/final-project-Mueller-Chandra/blob/master/figure13.png)](#features)


We then plotted the number of attacks in a particular year in a particular country against the age of that specific regime or a specific democracy, in doing so we wanted to examine the interaction between the two variables. As can be seen the regression does not explain the data very well, however there does appear to be a reduction in the number of terrorist attacks, the older the regime. 

[![figure14](https://github.com/erikemueller/final-project-Mueller-Chandra/blob/master/figure14.png)](#features)

[![figure15](https://github.com/erikemueller/final-project-Mueller-Chandra/blob/master/figure15.png)](#features)

The regression line appears to be slightly flatter when all the regimes are considered, as opposed to only democracies. In the figure with the age of democracies, it is interesting to note that there appears to be increased terrorism in countries that have existed as democracies for 60-80 years - which is perhaps indicative of increased terrorism amongst countries that were colonized but became independent around the 1930s and 40s.



## Something extra (& fun!)
Erik had another assignment that he used the STARTfinal.csv file that was generated for this project. The project created an interactive map that is hosted [here](https://erikemueller.shinyapps.io/hw10/) using R code. It is somewhat glitchy.
