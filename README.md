# surfs_up

## Overview of the analysis: 
This analysis uses SQLAlchemy to query a SQLite database in order to find temperature information in Oahu. The data is from the only the months of June and December from the years 2010-2017.

## Results: 
- Count: The first thing to note is that June and December have different data counts. There are 1700 entries for June and 1527 entries for December. 
- Mean: The mean for the months of June is 74.94. The mean for the month of December is 71.04. 
- Min/Max: In June the minimum temperature reached was 64, and the max was 85. In December minimum temperature reached was 56, and the max  was 83.

## Summary: 
Let's take a closer look at the results. 

The count is suprising because there are less days in June than there are in December, so it would make more sense if December had more data points than June. This will be adressed in the second bullet point below. 
It is expected for the December months to have an overall lower temperature than June. So the mean, min, and max temperatures all make sense.

 - Additional Query 1: The standard deviation in temperature for June is 3.26 but for December is 3.75. Why is that? Outliers? Let us provide a visual for the statistics provided in the *SurfsUp_Challenge.ipynb* file. Below are images containing both the code and the boxplots for the June & December temperatures. As is evident in the images, December has more outliers than June which explains why the standard deviation is higher.
     ![](June-boxplot.png)
     ![](Dec-boxplot.png)
 
 - Additional Query 2: The first bullet point in Results brings up an important point. The data count for June is about 200 more than the one for December although December has more days. My hypothesis is that when this data was sent, the year 2017 was not over yet, so the month of December did not have any entries. The code below looks to prove or disprove this theory.
```
j2017 = engine.execute("SELECT Measurement.date, Measurement.tobs FROM Measurement WHERE(Measurement.date BETWEEN '2017-06-01' AND '2017-06-30') ORDER BY Measurement.date").fetchall()

print(len(j2017))

print(j2017)
```
This first code block returns the amount of entries for June 2017 and prints out those results. 
There were 191 entries.
```
d2017 = engine.execute("SELECT Measurement.date, Measurement.tobs FROM Measurement WHERE(Measurement.date BETWEEN '2017-12-01' AND '2017-12-31') ORDER BY Measurement.date").fetchall()

print(len(d2017))

print(d2017)
 ```
 This second code block returns the amount of entries for December 2017 and prints out those results.
 There were 0 entries, and an empty list was returned proving my hypothesis correct.