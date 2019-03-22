#Visualizing USA Medal Counts by Edition: Line Plot
'''
Your job in this exercise is to visualize the medal counts by 'Edition' for the USA. The DataFrame has been pre-loaded for you as medals.

Instructions
100 XP
Create a DataFrame usa with data only for the USA.
Group usa such that ['Edition', 'Medal'] is the index. Aggregate the count over 'Athlete'.
Use .unstack() with level='Medal' to reshape the DataFrame usa_medals_by_year.
Construct a line plot from the final DataFrame usa_medals_by_year. This has been done for you, so hit 'Submit Answer' to see the plot!
'''

# Code
# Create the DataFrame: usa
usa = medals[medals.NOC == 'USA']

# Group usa by ['Edition', 'Medal'] and aggregate over 'Athlete'
usa_medals_by_year = usa.groupby(['Edition', 'Medal']).Athlete.count()

# Reshape usa_medals_by_year by unstacking
usa_medals_by_year = usa_medals_by_year.unstack(level='Medal')

# Plot the DataFrame usa_medals_by_year
usa_medals_by_year.plot()
plt.show()


'''


In [4]: usa.head()
Out[4]: 
      City  Edition      Sport Discipline         Athlete  NOC Gender         Event Event_gender   Medal
11  Athens     1896  Athletics  Athletics   LANE, Francis  USA    Men          100m            M  Bronze
13  Athens     1896  Athletics  Athletics   BURKE, Thomas  USA    Men          100m            M    Gold
15  Athens     1896  Athletics  Athletics  CURTIS, Thomas  USA    Men  110m hurdles            M    Gold
19  Athens     1896  Athletics  Athletics   BLAKE, Arthur  USA    Men         1500m            M  Silver
21  Athens     1896  Athletics  Athletics   BURKE, Thomas  USA    Men          400m            M    Gold


In [3]: usa_medals_by_year.head()
Out[3]: 
Medal    Bronze  Gold  Silver
Edition                      
1896          2    11       7
1900         14    27      14
1904        111   146     137
1908         15    34      14
1912         31    45      25

After unstack
In [7]: usa_medals_by_year
Out[7]: 
Medal   Edition
Bronze  1896         2
        1900        14
        1904       111
        1908        15
...
        2008        81
Gold    1896        11
        1900        27
        1904       146
  ...
        2004       116
        2008       125
Silver  1896         7
        1900        14
        1904       137
 ...
        1996        48
        2000        66
        2004        75
        2008       109
Length: 75, dtype: int64



'''
