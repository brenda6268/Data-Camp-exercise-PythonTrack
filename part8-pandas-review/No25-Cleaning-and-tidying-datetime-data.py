#Cleaning and tidying datetime data
'''
In order to use the full power of pandas time series, you must construct a DatetimeIndex. To do so, it is necessary to clean and transform the date and time columns.

The DataFrame df_dropped you created in the last exercise is provided for you and pandas has been imported as pd.

Your job is to clean up the date and Time columns and combine them into a datetime collection to be used as the Index.

Instructions
100 XP
Instructions
100 XP
Convert the 'date' column to a string with .astype(str) and assign to df_dropped['date'].
Add leading zeros to the 'Time' column. This has been done for you.
Concatenate the new 'date' and 'Time' columns together. Assign to date_string.
Convert the date_string Series to datetime values with pd.to_datetime(). Specify the format parameter.
Set the index of the df_dropped DataFrame to be date_times. Assign the result to df_clean.
'''

# Code
# Convert the date column to string: df_dropped['date']
df_dropped['date'] = df_dropped['date'].astype(str) #my error:.str is str method, not used to convert type.

# Pad leading zeros to the Time column: df_dropped['Time']
df_dropped['Time'] = df_dropped['Time'].apply(lambda x:'{:0>4}'.format(x))   #####

# Concatenate the new date and Time columns: date_string
date_string = df_dropped['date']+df_dropped['Time']

# Convert the date_string Series to datetime: date_times
date_times = pd.to_datetime(date_string, format='%Y%m%d%H%M')

# Set the index to be the new date_times container: df_clean
df_clean = df_dropped.set_index(date_times)

# Print the output of df_clean.head()
print(df_clean.head())

'''
 Wban      date  Time  StationType sky_condition  ... relative_humidity wind_speed wind_direction station_pressure sea_level_pressure
2011-01-01 00:53:00  13904  20110101  0053           12        OVC045  ...                24         15            360            29.42              29.95
2011-01-01 01:53:00  13904  20110101  0153           12        OVC049  ...                23         10            340            29.49              30.01
'''


'''my note
Before proceeding

In [1]: df_dropped.Time.head()
Out[1]: 
0     53
1    153
2    253
3    353
4    453
Name: Time, dtype: int64

In [3]: df_dropped.Time.head()
Out[3]: 
0    0053
1    0153
2    0253
3    0353
4    0453
Name: Time, dtype: object


'''