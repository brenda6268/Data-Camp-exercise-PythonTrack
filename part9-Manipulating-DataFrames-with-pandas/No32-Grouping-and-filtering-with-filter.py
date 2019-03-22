#Grouping and filtering with .filter()
'''
You can use groupby with the .filter() method to remove whole groups of rows from a DataFrame based on a boolean condition.

In this exercise, you'll take the February sales data and remove entries from companies that purchased less than or equal to 35 Units in the whole month.

First, you'll identify how many units each company bought for verification. Next you'll use the .filter() method after grouping by 'Company' to remove all rows belonging to companies whose sum over the 'Units' column was less than or equal to 35. Finally, verify that the three companies whose total Units purchased were less than or equal to 35 have been filtered out from the DataFrame.

Instructions
100 XP
Instructions
100 XP
Group sales by 'Company'. Save the result as by_company.
Compute and print the sum of the 'Units' column of by_company.
Call .filter() on by_company with lambda g:g['Units'].sum() > 35 as input and print the result.
'''

# Code
# Read the CSV file into a DataFrame: sales
sales = pd.read_csv('sales.csv', index_col='Date', parse_dates=True)

# Group sales by 'Company': by_company
by_company = sales.groupby('Company')

# Compute the sum of the 'Units' of by_company: by_com_sum
by_com_sum = by_company['Units'].sum()   #note: by_com_sum is a series object,not dataframe. 
print(by_com_sum)

# Filter 'Units' where the sum is > 35: by_com_filt
by_com_filt = by_company.filter(lambda g:g['Units'].sum() > 35)
print(by_com_filt) #by_com_filt is dataframe, and structure same as the original dataframe

'''
Company
Acme Coporation    34
Hooli              30
Initech            30
Mediacore          45
Streeplex          36
Name: Units, dtype: int64
                       Company   Product  Units
Date                                           
2015-02-02 21:00:00  Mediacore  Hardware      9
2015-02-04 15:30:00  Streeplex  Software     13
2015-02-09 09:00:00  Streeplex   Service     19
2015-02-09 13:00:00  Mediacore  Software      7
2015-02-19 11:00:00  Mediacore  Hardware     16
2015-02-19 16:00:00  Mediacore   Service     10
2015-02-21 05:00:00  Mediacore  Software      3
2015-02-26 09:00:00  Streeplex   Service      4
'''

'''
In [3]: sales
Out[3]: 
                             Company   Product  Units
Date                                                 
2015-02-02 08:30:00            Hooli  Software      3
2015-02-02 21:00:00        Mediacore  Hardware      9
2015-02-03 14:00:00          Initech  Software     13
2015-02-04 15:30:00        Streeplex  Software     13
2015-02-04 22:00:00  Acme Coporation  Hardware     14
2015-02-05 02:00:00  Acme Coporation  Software     19
2015-02-05 22:00:00            Hooli   Service     10
2015-02-07 23:00:00  Acme Coporation  Hardware      1
2015-02-09 09:00:00        Streeplex   Service     19
2015-02-09 13:00:00        Mediacore  Software      7
2015-02-11 20:00:00          Initech  Software      7
2015-02-11 23:00:00            Hooli  Software      4
2015-02-16 12:00:00            Hooli  Software     10
2015-02-19 11:00:00        Mediacore  Hardware     16
2015-02-19 16:00:00        Mediacore   Service     10
2015-02-21 05:00:00        Mediacore  Software      3
2015-02-21 20:30:00            Hooli  Hardware      3
2015-02-25 00:30:00          Initech   Service     10
2015-02-26 09:00:00        Streeplex   Service      4


In [7]: print(by_company.groups.keys())   #by_comany is dict
dict_keys(['Acme Coporation', 'Hooli', 'Initech', 'Mediacore', 'Streeplex'])

In [11]: by_company.groups.items()
Out[11]: dict_items([('Acme Coporation', DatetimeIndex(['2015-02-04 22:00:00', '2015-02-05 02:00:00', '2015-02-07 23:00:00'], dtype='datetime64[ns]', name='Date', freq=None)), ('Hooli', DatetimeIndex(['2015-02-02 08:30:00', '2015-02-05 22:00:00', '2015-02-11 23:00:00', '2015-02-16 12:00:00', '2015-02-21 20:30:00'], dtype='datetime64[ns]', name='Date', freq=None)), ('Initech', DatetimeIndex(['2015-02-03 14:00:00', '2015-02-11 20:00:00', '2015-02-25 00:30:00'], dtype='datetime64[ns]', name='Date', freq=None)), ('Mediacore', DatetimeIndex(['2015-02-02 21:00:00', '2015-02-09 13:00:00', '2015-02-19 11:00:00', '2015-02-19 16:00:00', '2015-02-21 05:00:00'], dtype='datetime64[ns]', name='Date', freq=None)), ('Streeplex', DatetimeIndex(['2015-02-04 15:30:00', '2015-02-09 09:00:00', '2015-02-26 09:00:00'], dtype='datetime64[ns]', name='Date', freq=None))])

In [12]: by_company.groups.get('Mediacore')
Out[12]: DatetimeIndex(['2015-02-02 21:00:00', '2015-02-09 13:00:00', '2015-02-19 11:00:00', '2015-02-19 16:00:00', '2015-02-21 05:00:00'], dtype='datetime64[ns]', name='Date', freq=None)


In [14]: type(by_com_sum)
Out[14]: pandas.core.series.Series
'''