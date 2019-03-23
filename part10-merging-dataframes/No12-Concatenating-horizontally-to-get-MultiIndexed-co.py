#Concatenating horizontally to get MultiIndexed columns
'''
It is also possible to construct a DataFrame with hierarchically indexed columns. For this exercise, you'll start with pandas imported and a list of three DataFrames called dataframes. All three DataFrames contain 'Company', 'Product', and 'Units' columns with a 'Date' column as the index pertaining to sales transactions during the month of February, 2015. The first DataFrame describes Hardware transactions, the second describes Software transactions, and the third, Service transactions.

Your task is to concatenate the DataFrames horizontally and to create a MultiIndex on the columns. From there, you can summarize the resulting DataFrame and slice some information from it.

Instructions
100 XP
Instructions
100 XP
Construct a new DataFrame february with MultiIndexed columns by concatenating the list dataframes.
Use axis=1 to stack the DataFrames horizontally and the keyword argument keys=['Hardware', 'Software', 'Service'] to construct a hierarchical Index from each DataFrame.
Print summary information from the new DataFrame february using the .info() method. This has been done for you.
Create an alias called idx for pd.IndexSlice.
Extract a slice called slice_2_8 from february (using .loc[] & idx) that comprises rows between Feb. 2, 2015 to Feb. 8, 2015 from columns under 'Company'.
Print the slice_2_8. This has been done for you, so hit 'Submit Answer' to see the sliced data!
'''

# Code
# Concatenate dataframes: february
february = pd.concat(dataframes, axis=1,keys=['Hardware', 'Software', 'Service'])

# Print february.info()
print(february.info())

# Assign pd.IndexSlice: idx
idx = pd.IndexSlice

# Create the slice: slice_2_8
slice_2_8 = february.loc['Feb. 2, 2015':'Feb. 8, 2015', idx[:, 'Company']]

# Print slice_2_8
print(slice_2_8)

'''
<class 'pandas.core.frame.DataFrame'>
DatetimeIndex: 20 entries, 2015-02-02 08:33:01 to 2015-02-26 08:58:51
Data columns (total 9 columns):
(Hardware, Company)    5 non-null object
(Hardware, Product)    5 non-null object
(Hardware, Units)      5 non-null float64
(Software, Company)    9 non-null object
(Software, Product)    9 non-null object
(Software, Units)      9 non-null float64
(Service, Company)     6 non-null object
(Service, Product)     6 non-null object
(Service, Units)       6 non-null float64
dtypes: float64(3), object(6)
memory usage: 1.6+ KB
None
                            Hardware         Software Service
                             Company          Company Company
Date                                                         
2015-02-02 08:33:01              NaN            Hooli     NaN
2015-02-02 20:54:49        Mediacore              NaN     NaN
2015-02-03 14:14:18              NaN          Initech     NaN
2015-02-04 15:36:29              NaN        Streeplex     NaN
2015-02-04 21:52:45  Acme Coporation              NaN     NaN
2015-02-05 01:53:06              NaN  Acme Coporation     NaN
2015-02-05 22:05:03              NaN              NaN   Hooli
2015-02-07 22:58:10  Acme Coporation              NaN     NaN
'''


'''
In [2]: february
Out[2]: 
                            Hardware                         Software                    Service               
                             Company   Product Units          Company   Product Units    Company  Product Units
Date                                                                                                           
2015-02-02 08:33:01              NaN       NaN   NaN            Hooli  Software   3.0        NaN      NaN   NaN
2015-02-02 20:54:49        Mediacore  Hardware   9.0              NaN       NaN   NaN        NaN      NaN   NaN
2015-02-03 14:14:18              NaN       NaN   NaN          Initech  Software  13.0        NaN      NaN   NaN
2015-02-04 15:36:29              NaN       NaN   NaN        Streeplex  Software  13.0        NaN      NaN   NaN
2015-02-04 21:52:45  Acme Coporation  Hardware  14.0              NaN       NaN   NaN        NaN      NaN   NaN
2015-02-05 01:53:06              NaN       NaN   NaN  Acme Coporation  Software  19.0        NaN      NaN   NaN
2015-02-05 22:05:03              NaN       NaN   NaN              NaN       NaN   NaN      Hooli  Service  10.0
2015-02-07 22:58:10  Acme Coporation  Hardware   1.0              NaN       NaN   NaN        NaN      NaN   NaN
2015-02-09 08:57:30              NaN       NaN   NaN              NaN       NaN   NaN  Streeplex  Service  19.0
2015-02-09 13:09:55              NaN       NaN   NaN        Mediacore  Software   7.0        NaN      NaN   NaN
2015-02-11 20:03:08              NaN       NaN   NaN          Initech  Software   7.0        NaN      NaN   NaN
2015-02-11 22:50:44              NaN       NaN   NaN            Hooli  Software   4.0        NaN      NaN   NaN
2015-02-16 12:09:19              NaN       NaN   NaN            Hooli  Software  10.0        NaN      NaN   NaN
2015-02-19 10:59:33        Mediacore  Hardware  16.0              NaN       NaN   NaN        NaN      NaN   NaN
2015-02-19 16:02:58              NaN       NaN   NaN              NaN       NaN   NaN  Mediacore  Service  10.0
2015-02-21 05:01:26              NaN       NaN   NaN        Mediacore  Software   3.0        NaN      NaN   NaN
2015-02-21 20:41:47            Hooli  Hardware   3.0              NaN       NaN   NaN        NaN      NaN   NaN
2015-02-25 00:29:00              NaN       NaN   NaN              NaN       NaN   NaN    Initech  Service  10.0
2015-02-26 08:57:45              NaN       NaN   NaN              NaN       NaN   NaN  Streeplex  Service   4.0
2015-02-26 08:58:51              NaN       NaN   NaN              NaN       NaN   NaN  Streeplex  Service   1.0




'''
