#Concatenating pandas Series along row axis
'''
Having learned how to append Series, you'll now learn how to achieve the same result by concatenating Series instead. You'll continue to work with the sales data you've seen previously. This time, the DataFrames jan, feb, and mar have been pre-loaded.

Your job is to use pd.concat() with a list of Series to achieve the same result that you would get by chaining calls to .append().

You may be wondering about the difference between pd.concat() and pandas' .append() method. One way to think of the difference is that .append() is a specific case of a concatenation, while pd.concat() gives you more flexibility, as you'll see in later exercises.

Instructions
100 XP
Instructions
100 XP
Create an empty list called units. This has been done for you.
Use a for loop to iterate over [jan, feb, mar]:
In each iteration of the loop, append the 'Units' column of each DataFrame to units.
Concatenate the Series contained in the list units into a longer Series called quarter1 using pd.concat().
Specify the keyword argument axis='rows' to stack the Series vertically.
Verify that quarter1 has the individual Series stacked vertically by printing slices. This has been done for you, so hit 'Submit Answer' to see the result!
'''

# Code

# Initialize empty list: units
units = []

# Build the list of Series
for month in [jan, feb, mar]:
    units.append(month['Units'])  
    #In [7]: len(units)
     #Out[7]: 3

# Concatenate the list: quarter1
quarter1 = pd.concat(units, axis='rows')

#In [10]: type(quarter1)
#Out[10]: pandas.core.series.Series

# Print slices from quarter1
print(quarter1.loc['jan 27, 2015':'feb 2, 2015'])
print(quarter1.loc['feb 26, 2015':'mar 7, 2015'])

'''
Date
2015-01-27 07:11:55    18
2015-02-02 08:33:01     3
2015-02-02 20:54:49     9
Name: Units, dtype: int64
Date
2015-02-26 08:57:45     4
2015-02-26 08:58:51     1
2015-03-06 10:11:45    17
2015-03-06 02:03:56    17
Name: Units, dtype: int64


'''
'''
In [3]: jan
Out[3]: 
                             Company   Product  Units
Date                                                 
2015-01-21 19:13:21        Streeplex  Hardware     11
2015-01-09 05:23:51        Streeplex   Service      8
2015-01-06 17:19:34          Initech  Hardware     17
2015-01-02 09:51:06            Hooli  Hardware     16
2015-01-11 14:51:02            Hooli  Hardware     11
2015-01-01 07:31:20  Acme Coporation  Software     18
2015-01-24 08:01:16          Initech  Software      1
2015-01-25 15:40:07          Initech   Service      6
2015-01-13 05:36:12            Hooli   Service      7
2015-01-03 18:00:19            Hooli   Service     19
2015-01-16 00:33:47            Hooli  Hardware     17
2015-01-16 07:21:12          Initech   Service     13
2015-01-20 19:49:24  Acme Coporation  Hardware     12
2015-01-26 01:50:25  Acme Coporation  Software     14
2015-01-15 02:38:25  Acme Coporation   Service     16
2015-01-06 13:47:37  Acme Coporation  Software     16
2015-01-15 15:33:40        Mediacore  Hardware      7
2015-01-27 07:11:55        Streeplex   Service     18
2015-01-20 11:28:02        Streeplex  Software     13
2015-01-16 19:20:46        Mediacore   Service      8



In [5]: type(units)
Out[5]: list

In [7]: len(units)
Out[7]: 3

'''