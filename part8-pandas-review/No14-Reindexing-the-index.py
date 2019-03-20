#Reindexing the Index
'''
Reindexing is useful in preparation for adding or otherwise combining two time series data sets. To reindex the data, we provide a new index and ask pandas to try and match the old data to the new index. If data is unavailable for one of the new index dates or times, you must tell pandas how to fill it in. Otherwise, pandas will fill with NaN by default.

In this exercise, two time series data sets containing daily data have been pre-loaded for you, each indexed by dates. The first, ts1, includes weekends, but the second, ts2, does not. The goal is to combine the two data sets in a sensible way. Your job is to reindex the second data set so that it has weekends as well, and then add it to the first. When you are done, it would be informative to inspect your results.

Instructions
100 XP
Instructions
100 XP
Create a new time series ts3 by reindexing ts2 with the index of ts1. To do this, call .reindex() on ts2 and pass in the index of ts1 (ts1.index).
Create another new time series, ts4, by calling the same .reindex() as above, but also specifiying a fill method, using the keyword argument method="ffill" to forward-fill values.
Add ts1 + ts2. Assign the result to sum12.
Add ts1 + ts3. Assign the result to sum13.
Add ts1 + ts4, Assign the result to sum14.
'''

# Code
# Reindex without fill method: ts3
ts3 = ts2.reindex(ts1.index)

# Reindex with fill method, using forward fill: ts4
ts4 = ts2.reindex(ts1.index, method='ffill')

# Combine ts1 + ts2: sum12, my note: ts2 no weekend, so in the weekend of sum12 is null
sum12 = ts1+ts2

# Combine ts1 + ts3: sum13  , my note :  assert sum12.all()== sum13.all()  cannot use sum12==sum13
sum13 = ts1+ts3

# Combine ts1 + ts4: sum14, my note: 
sum14 = ts1+ts4


'''result
In [15]: ts1.head(5)
Out[15]: 
2016-07-01    0
2016-07-02    1
2016-07-03    2
2016-07-04    3
2016-07-05    4
dtype: int64



'''