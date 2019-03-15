#Reshaping your data
'''
Now that you have all the data combined into a single DataFrame, the next step is to reshape it into a tidy data format.

Currently, the gapminder DataFrame has a separate column for each year. What you want instead is a single column that contains the year, and a single column that represents the average life expectancy for each year and country. By having year in its own column, you can use it as a predictor variable in a later analysis.

You can convert the DataFrame into the desired tidy format by melting it.

Instructions
100 XP
Reshape gapminder by melting it. Keep 'Life expectancy' fixed by specifying it as an argument to the id_vars parameter.
Rename the three columns of the melted DataFrame to 'country', 'year', and 'life_expectancy' by passing them in as a list to gapminder_melt.columns.
Print the head of the melted DataFrame.
'''

# Code
import pandas as pd

# Melt gapminder: gapminder_melt
gapminder_melt = pd.melt(frame=gapminder,id_vars=['Life expectancy'])

# Rename the columns
gapminder_melt.columns = ['country', 'year',  'life_expectancy']

# Print the head of gapminder_melt
print(gapminder_melt.head())



'''result
                 country  year  life_expectancy
0               Abkhazia  1800              NaN
1            Afghanistan  1800            28.21
2  Akrotiri and Dhekelia  1800              NaN
3                Albania  1800            35.40
4                Algeria  1800            28.82


'''

'''
In [2]: gapminder.head()
Out[2]: 
    1800   1801   1802   1803   1804          ...            2013  2014  2015  2016        Life expectancy
0    NaN    NaN    NaN    NaN    NaN          ...             NaN   NaN   NaN   NaN               Abkhazia
1  28.21  28.20  28.19  28.18  28.17          ...             NaN   NaN   NaN   NaN            Afghanistan
2    NaN    NaN    NaN    NaN    NaN          ...             NaN   NaN   NaN   NaN  Akrotiri and Dhekelia
3  35.40  35.40  35.40  35.40  35.40          ...             NaN   NaN   NaN   NaN                Albania
4  28.82  28.82  28.82  28.82  28.82          ...             NaN   NaN   NaN   NaN                Algeria

[5 rows x 218 columns]
'''