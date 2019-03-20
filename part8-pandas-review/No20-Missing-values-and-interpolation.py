#Missing values and interpolation
'''
One common application of interpolation in data analysis is to fill in missing data.

In this exercise, noisy measured data that has some dropped or otherwise missing values has been loaded. The goal is to compare two time series, and then look at summary statistics of the differences. The problem is that one of the data sets is missing data at some of the times. The pre-loaded data ts1 has value for all times, yet the data set ts2 does not: it is missing data for the weekends.

Your job is to first interpolate to fill in the data for all days. Then, compute the differences between the two data sets, now that they both have full support for all times. Finally, generate the summary statistics that describe the distribution of differences.

Instructions
100 XP
Instructions
100 XP
Replace the index of ts2 with that of ts1, and then fill in the missing values of ts2 by using .interpolate(how='linear'). Save the result as ts2_interp.
Compute the difference between ts1 and ts2_interp. Take the absolute value of the difference with np.abs(), and assign the result to differences.
Generate and print summary statistics of the differences with .describe() and print().
'''

# Code
# Reset the index of ts2 to ts1, and then use linear interpolation to fill in the NaNs: ts2_interp
ts2_interp = ts2.reindex(ts1.index).interpolate(how='linear')

# Compute the absolute difference of ts1 and ts2_interp: differences 
differences = np.abs(ts1-ts2_interp)

# Generate and print summary statistics of the differences
print(differences.describe())

'''result
count    17.000000
mean      2.882353
std       1.585267
min       0.000000
25%       2.000000
50%       2.666667
75%       4.000000
max       6.000000
dtype: float64

'''

'''
In [5]: ts1.head()
Out[5]: 
2016-07-01    0
2016-07-02    1
2016-07-03    2
2016-07-04    3
2016-07-05    4
dtype: int64



In [2]: ts2.head()
Out[2]: 
2016-07-01    0
2016-07-04    1
2016-07-05    2
2016-07-06    3
2016-07-07    4
dtype: int64


In [3]: ts2_interp.head()
Out[3]: 
2016-07-01    0.000000
2016-07-02    0.333333
2016-07-03    0.666667
2016-07-04    1.000000
2016-07-05    2.000000
dtype: float64


In [4]: differences.head()
Out[4]: 
2016-07-01    0.000000
2016-07-02    0.666667
2016-07-03    1.333333
2016-07-04    2.000000
2016-07-05    2.000000
dtype: float64

'''