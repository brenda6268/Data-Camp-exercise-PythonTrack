#Creating and using a DatetimeIndex
The pandas Index is a powerful way to handle time series data, so it is valuable to know how to build one yourself. Pandas provides the pd.to_datetime() function for just this task. For example, if passed the list of strings ['2015-01-01 091234','2015-01-01 091234'] and a format specification variable, such as format='%Y-%m-%d %H%M%S, pandas will parse the string into the proper datetime elements and build the datetime objects.

In this exercise, a list of temperature data and a list of date strings has been pre-loaded for you as temperature_list and date_list respectively. Your job is to use the .to_datetime() method to build a DatetimeIndex out of the list of date strings, and to then use it along with the list of temperature data to build a pandas Series.
#Instructions
100 XP
Prepare a format string, time_format, using '%Y-%m-%d %H:%M' as the desired format.
Convert date_list into a datetime object by using the pd.to_datetime() function. Specify the format string you defined above and assign the result to my_datetimes.
Construct a pandas Series called time_series using pd.Series() with temperature_list and my_datetimes. Set the index of the Series to be my_datetimes.
'''

#Instructions
100 XP
Prepare a format string, time_format, using '%Y-%m-%d %H:%M' as the desired format.
Convert date_list into a datetime object by using the pd.to_datetime() function. Specify the format string you defined above and assign the result to my_datetimes.
Construct a pandas Series called time_series using pd.Series() with temperature_list and my_datetimes. Set the index of the Series to be my_datetimes.
'''

# Code
# Prepare a format string: time_format
time_format = '%Y-%m-%d %H:%M'#don't find out the difference from '%Y-%m-%d %H'

# Convert date_list into a datetime object: my_datetimes
my_datetimes = pd.to_datetime(date_list, format=time_format)  

# Construct a pandas Series using temperature_list and my_datetimes: time_series
time_series = pd.Series(temperature_list, index=my_datetimes)


'''result


In [16]: pd.Series(temperature_list, index=my_datetimes)
Out[16]: 
2010-01-01 00:00:00    46.2
2010-01-01 01:00:00    44.6
2010-01-01 02:00:00    44.1
2010-01-01 03:00:00    43.8
2010-01-01 04:00:00    43.5
2010-01-01 05:00:00    43.0
2010-01-01 06:00:00    43.1
2010-01-02 04:00:00    43.9
2010-01-02 05:00:00    43.3
                       ... 

2010-12-31 16:00:00    58.8
2010-12-31 17:00:00    57.6
2010-12-31 18:00:00    54.3
2010-12-31 19:00:00    51.1
2010-12-31 20:00:00    49.0
2010-12-31 21:00:00    47.9
2010-12-31 22:00:00    46.9
2010-12-31 23:00:00    46.2
Length: 8759, dtype: float64


'''




'''my note
In [21]: df3=df1.head()

In [22]: df3
Out[22]: 
   Temperature  DewPoint  Pressure            Date
0         46.2      37.5       1.0  20100101 00:00
1         44.6      37.1       1.0  20100101 01:00
2         44.1      36.9       1.0  20100101 02:00
3         43.8      36.9       1.0  20100101 03:00
4         43.5      36.8       1.0  20100101 04:00


In [23]: df3['Cdate']='2010'

In [24]: df3
Out[24]: 
   Temperature  DewPoint  Pressure            Date Cdate
0         46.2      37.5       1.0  20100101 00:00  2010
1         44.6      37.1       1.0  20100101 01:00  2010
2         44.1      36.9       1.0  20100101 02:00  2010
3         43.8      36.9       1.0  20100101 03:00  2010
4         43.5      36.8       1.0  20100101 04:00  2010


In [28]: df3['Cdate']=pd.to_datetime(df3['Cdate'])

In [29]: df3
Out[29]: 
   Temperature  DewPoint  Pressure            Date      Cdate
0         46.2      37.5       1.0  20100101 00:00 2010-01-01
1         44.6      37.1       1.0  20100101 01:00 2010-01-01
2         44.1      36.9       1.0  20100101 02:00 2010-01-01
3         43.8      36.9       1.0  20100101 03:00 2010-01-01
4         43.5      36.8       1.0  20100101 04:00 2010-01-01


problem:no value after reindex
In [31]: df3.reindex(df3['Cdate'])
Out[31]: 
            Temperature  DewPoint  Pressure Date Cdate
Cdate                                                 
2010-01-01          NaN       NaN       NaN  NaN   NaT
2010-01-01          NaN       NaN       NaN  NaN   NaT
2010-01-01          NaN       NaN       NaN  NaN   NaT
2010-01-01          NaN       NaN       NaN  NaN   NaT
2010-01-01          NaN       NaN       NaN  NaN   NaT
'''