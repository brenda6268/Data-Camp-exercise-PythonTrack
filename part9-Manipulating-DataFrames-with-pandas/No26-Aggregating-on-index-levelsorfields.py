#Aggregating on index levels/fields
'''
If you have a DataFrame with a multi-level row index, the individual levels can be used to perform the groupby. This allows advanced aggregation techniques to be applied along one or more levels in the index and across one or more columns.

In this exercise you'll use the full Gapminder dataset which contains yearly values of life expectancy, population, child mortality (per 1,000) and per capita gross domestic product (GDP) for every country in the world from 1964 to 2013.

Your job is to create a multi-level DataFrame of the columns 'Year', 'Region' and 'Country'. Next you'll group the DataFrame by the 'Year' and 'Region' levels. Finally, you'll apply a dictionary aggregation to compute the total population, spread of per capita GDP values and average child mortality rate.

The Gapminder CSV file is available as 'gapminder.csv'.

Instructions
100 XP
Read 'gapminder.csv' into a DataFrame with index_col=['Year','region','Country']. Sort the index.
Group gapminder with a level of ['Year','region'] using its level parameter. Save the result as by_year_region.
Define the function spread which returns the maximum and minimum of an input series. This has been done for you.
Create a dictionary with 'population':'sum', 'child_mortality':'mean' and 'gdp':spread as aggregator. This has been done for you.
Use the aggregator dictionary to aggregate by_year_region. Save the result as aggregated.
Print the last 6 entries of aggregated. This has been done for you, so hit 'Submit Answer' to view the result.
'''

# Code
# Read the CSV file into a DataFrame and sort the index: gapminder
gapminder = pd.read_csv('gapminder.csv',index_col=['Year','region','Country']).sort_index()

# Group gapminder by 'Year' and 'region': by_year_region
#by_year_region = gapminder.groupby(['Year', 'region'])  No1 output
by_year_region = gapminder.groupby(level=['Year', 'region']) # no2 output

# Define the function to compute spread: spread
def spread(series):
    return series.max() - series.min()

# Create the dictionary: aggregator
aggregator = {'population':'sum', 'child_mortality':'mean', 'gdp':spread}

# Aggregate by_year_region using the dictionary: aggregated
aggregated = by_year_region.agg(aggregator)

# Print the last 6 entries of aggregated 
print(aggregated.tail(6))

''' 
#no1 output
                                   population  child_mortality       gdp
Year region                                                             
2013 America                     9.629087e+08        17.745833   49634.0
     East Asia & Pacific         2.244209e+09        22.285714  134744.0
     Europe & Central Asia       8.968788e+08         9.831875   86418.0
     Middle East & North Africa  4.030504e+08        20.221500  128676.0
     South Asia                  1.701241e+09        46.287500   11469.0
     Sub-Saharan Africa          9.205996e+08        76.944490   32035.0

'''

'''
add level in by_year_region = gapminder.groupby(level=['Year', 'region']))
#no2 output

                                   population  child_mortality       gdp
Year region                                                             
2013 America                     9.629087e+08        17.745833   49634.0
     East Asia & Pacific         2.244209e+09        22.285714  134744.0
     Europe & Central Asia       8.968788e+08         9.831875   86418.0
     Middle East & North Africa  4.030504e+08        20.221500  128676.0
     South Asia                  1.701241e+09        46.287500   11469.0
     Sub-Saharan Africa          9.205996e+08        76.944490   32035.0

'''

'''
In [2]: gapminder.head()
Out[2]: 
                                  fertility    life  population  child_mortality      gdp
Year region  Country                                                                     
1964 America Antigua and Barbuda      4.250  63.775     58653.0            72.78   5008.0
             Argentina                3.068  65.388  21966478.0            57.43   8227.0
             Aruba                    4.059  67.113     57031.0              NaN   5505.0
             Bahamas                  4.220  64.189    133709.0            48.56  18160.0
             Barbados                 4.094  62.819    234455.0            64.70   5681.0


'''