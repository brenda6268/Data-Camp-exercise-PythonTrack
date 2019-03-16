#Quantiles
'''
In this exercise, you'll investigate the probabilities of life expectancy in countries around the world. This dataset contains life expectancy for persons born each year from 1800 to 2015. Since country names change or results are not reported, not every country has values. This dataset was obtained from Gapminder.

First, you will determine the number of countries reported in 2015. There are a total of 260 unique countries in the entire dataset. Then, you will compute the 5th and 95th percentiles of life expectancy over the entire dataset. Finally, you will make a box plot of life expectancy every 50 years from 1800 to 2000. Notice the large change in the distributions over this period.

The dataset has been pre-loaded into a DataFrame called df.
#Instructions
100 XP
Print the number of countries reported in 2015. To do this, use the .count() method on the '2015' column of df.
Print the 5th and 95th percentiles of df. To do this, use the .quantile() method with the list [0.05, 0.95].
Generate a box plot using the list of columns provided in years. This has already been done for you, so click on 'Submit Answer' to view the result!
'''

# Code
# Print the number of countries reported in 2015
print(df['2015'].count())

# Print the 5th and 95th percentiles
print(df.quantile([0.05,0.95]))  #note, in the .quantile() should use list[]

# Generate a box plot
years = ['1800','1850','1900','1950','2000']
df[years].plot(kind='box')
plt.show()

'''result
208
      Unnamed: 0   1800   1801   1802  1803  ...    2012    2013   2014    2015     2016
0.05       12.95  25.40  25.30  25.20  25.2  ...  56.335  56.705  56.87  57.855  59.2555
0.95      246.05  37.92  37.35  38.37  38.0  ...  81.665  81.830  82.00  82.100  82.1650

[2 rows x 218 columns]

'''