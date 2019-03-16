#Bachelor's degrees awarded to women
'''
In this exercise, you will investigate statistics of the percentage of Bachelor's degrees awarded to women from 1970 to 2011. Data is recorded every year for 17 different fields. This data set was obtained from the Digest of Education Statistics.

Your job is to compute the minimum and maximum values of the 'Engineering' column and generate a line plot of the mean value of all 17 academic fields per year. To perform this step, you'll use the .mean() method with the keyword argument axis='columns'. This computes the mean across all columns per row.

The DataFrame has been pre-loaded for you as df with the index set to 'Year'.
#Instructions
100 XP
Print the minimum value of the 'Engineering' column.
Print the maximum value of the 'Engineering' column.
Construct the mean percentage per year with .mean(axis='columns'). Assign the result to mean.
Plot the average percentage per year. Since 'Year' is the index of df, it will appear on the x-axis of the plot. No keyword arguments are needed in your call to .plot().
'''

# Code
# Print the minimum value of the Engineering column
print(df['Engineering'].min())

# Print the maximum value of the Engineering column
print(df['Engineering'].max())

# Construct the mean percentage per year: mean
mean = df.mean(axis='columns')

# Plot the average percentage per year
mean.plot()
#df.plot()

# Display the plot
plt.show()


'''result
0.8
19.0
'''
'''
In [6]: df.head()
Out[6]: 
      Agriculture  Architecture  Art and Performance    Biology   Business  ...  Math and Statistics  Physical Sciences  Psychology  Public Administration  Social Sciences and History
Year                                                                        ...                                                                                                        
1970     4.229798     11.921005                 59.7  29.088363   9.064439  ...                 38.0               13.8        44.4                   68.4                         36.8
1971     5.452797     12.003106                 59.9  29.394403   9.503187  ...                 39.0               14.9        46.2                   65.5                         36.2
1972     7.420710     13.214594                 60.4  29.810221  10.558962  ...                 40.2               14.8        47.6                   62.6                         36.1
1973     9.653602     14.791613                 60.2  31.147915  12.804602  ...                 40.9               16.5        50.4                   64.3                         36.4
1974    14.074623     17.444688                 61.9  32.996183  16.204850  ...                 41.8               18.2        52.6                   66.1                         37.3

[5 rows x 17 columns]


In [7]: df.mean()
Out[7]: 
Agriculture                      33.848165
Architecture                     33.685540
Art and Performance              61.100000
Biology                          49.429864
Business                         40.653471
Communications and Journalism    56.216667
Computer Science                 25.809524
Education                        76.356236
Engineering                      12.892857
English                          66.186680
Foreign Languages                71.723810
Health Professions               82.983333
Math and Statistics              44.478571
Physical Sciences                31.304762
Psychology                       68.776190
Public Administration            76.085714
Social Sciences and History      45.407143
dtype: float64


In [9]: df.mean(axis='columns')   #same as df.mean(axis=1)
Out[9]: 
Year
1970    38.594697
1971    38.603481
1972    39.066075
1973    40.131826
1974    41.715916
1975    42.373672
1976    44.015581
1977    45.673823
1978    47.308670
1979    48.811798
1980    49.980583
1981    50.974090
1982    52.009448
1983    52.187399
1984    52.474007
1985    52.399548
1986    52.752830
1987    53.169798
1988    53.130635
1989    53.305542
1990    53.737364
1991    53.471622
1992    53.262399
1993    53.199202
1994    53.238427
1995    53.508401
1996    53.941559
1997    54.446953
1998    55.227195
1999    55.971538
2000    56.501939
2001    56.946913
2002    57.181722
2003    57.367542
2004    57.019094
2005    56.723782
2006    56.262194
2007    56.053781
2008    55.903924
2009    56.026406
2010    55.883043
2011    55.999587
dtype: float64









'''