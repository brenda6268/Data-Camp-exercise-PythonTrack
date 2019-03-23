#Resampling & concatenating DataFrames with inner join
'''
In this exercise, you'll compare the historical 10-year GDP (Gross Domestic Product) growth in the US and in China. The data for the US starts in 1947 and is recorded quarterly; by contrast, the data for China starts in 1961 and is recorded annually.

You'll need to use a combination of resampling and an inner join to align the index labels. You'll need an appropriate offset alias for resampling, and the method .resample() must be chained with some kind of aggregation method (.pct_change() and .last() in this case).

pandas has been imported as pd, and the DataFrames china and us have been pre-loaded, with the output of china.head() and us.head() printed in the IPython Shell.

Instructions
70 XP

Make a new DataFrame china_annual by resampling the DataFrame china with .resample('A').last() (i.e., with annual frequency) and chaining two method calls:
Chain .pct_change(10) as an aggregation method to compute the percentage change with an offset of ten years.
Chain .dropna() to eliminate rows containing null values.
Make a new DataFrame us_annual by resampling the DataFrame us exactly as you resampled china.
Concatenate china_annual and us_annual to construct a DataFrame called gdp. Use join='inner' to perform an inner join and use axis=1 to concatenate horizontally.
Print the result of resampling gdp every decade (i.e., using .resample('10A')) and aggregating with the method .last(). This has been done for you, so hit 'Submit Answer' to see the result!
'''

# Code
# Resample and tidy china: china_annual
china_annual = china.resample('A').last().pct_change(10).dropna()
# china.resample('A').pct_change(10).dropna()

# Resample and tidy us: us_annual
us_annual = us.resample('A').last().pct_change(10).dropna()
#us.resample('A').pct_change(10).dropna()

# Concatenate china_annual and us_annual: gdp
gdp = pd.concat([china_annual,us_annual],join='inner',axis=1)

# Resample gdp and print
print(gdp.resample('10A').last())

'''result
<script.py> output:
                   China        US
    Year                          
    1971-12-31  0.988860  1.052270
    1981-12-31  0.972048  1.750922
    1991-12-31  0.962528  0.912380
    2001-12-31  2.492511  0.704219
    2011-12-31  4.623958  0.475082
    2021-12-31  3.789936  0.361780

'''

'''
In [6]: china.resample('A').last()
Out[6]: 
                   China
Year                    
1961-12-31     49.557050
1962-12-31     46.685179
1963-12-31     50.097303
1964-12-31     59.062255
...
2008-12-31   4558.431073
2009-12-31   5059.419738
2010-12-31   6039.658508
2011-12-31   7492.432098
2012-12-31   8461.623163
2013-12-31   9490.602600
2014-12-31  10351.111762
2015-12-31  10866.443998


In [10]: us
Out[10]: 
                 US
Year               
1947-04-01    246.3
1947-07-01    250.1
1947-10-01    260.3
1948-01-01    266.2
...

In [11]: us.resample('A').last()
Out[11]: 
                 US
Year               
1947-12-31    260.3
1948-12-31    280.7
1949-12-31    271.0
...



'''
