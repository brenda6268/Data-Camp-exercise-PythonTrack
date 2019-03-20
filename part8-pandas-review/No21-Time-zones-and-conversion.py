#Time zones and conversion
'''
Time zone handling with pandas typically assumes that you are handling the Index of the Series. In this exercise, you will learn how to handle timezones that are associated with datetimes in the column data, and not just the Index.

You will work with the flight departure dataset again, and this time you will select Los Angeles ('LAX') as the destination airport.

Here we will use a mask to ensure that we only compute on data we actually want. To learn more about Boolean masks, click here!

Instructions
100 XP
Instructions
100 XP
Create a Boolean mask, mask, such that if the 'Destination Airport' column of df equals 'LAX', the result is True, and otherwise, it is False.
Use the mask to extract only the LAX rows. Assign the result to la.
Concatenate the two columns la['Date (MM/DD/YYYY)'] and la['Wheels-off Time'] with a ' ' space in between. Pass this to pd.to_datetime() to create a datetime array of all the times the LAX-bound flights left the ground.
Use Series.dt.tz_localize() to localize the time to 'US/Central'.
Use the .dt.tz_convert() method to convert datetimes from 'US/Central' to 'US/Pacific'.
'''

# Code
# Build a Boolean mask to filter out all the 'LAX' departure flights: mask
mask = df['Destination Airport'] == 'LAX'

# Use the mask to subset the data: la
la = df[mask]

# Combine two columns of data to create a datetime series: times_tz_none 
times_tz_none = pd.to_datetime( la['Date (MM/DD/YYYY)'] + ' ' + la['Wheels-off Time'] )

# Localize the time to US/Central: times_tz_central
times_tz_central = times_tz_none.dt.tz_localize('US/Central')

# Convert the datetimes from US/Central to US/Pacific
times_tz_pacific = times_tz_central.dt.tz_convert('US/Pacific')


'''note
#With the tz=None, we can remove the time zone information while keeping the local time (not converted to UTC):

>>> tz_aware.tz_localize(None)





In [4]: times_tz_none
Out[4]: 
33     2015-07-01 05:43:00
55     2015-07-01 16:27:00
91     2015-07-02 05:47:00
113    2015-07-02 16:23:00
134    2015-07-03 05:30:00
...

In [6]: times_tz_central.head()
Out[6]: 
33    2015-07-01 05:43:00-05:00
55    2015-07-01 16:27:00-05:00
91    2015-07-02 05:47:00-05:00
113   2015-07-02 16:23:00-05:00
134   2015-07-03 05:30:00-05:00
dtype: datetime64[ns, US/Central]

In [7]: times_tz_pacific.head()
Out[7]: 
33    2015-07-01 03:43:00-07:00
55    2015-07-01 14:27:00-07:00
91    2015-07-02 03:47:00-07:00
113   2015-07-02 14:23:00-07:00
134   2015-07-03 03:30:00-07:00
dtype: datetime64[ns, US/Pacific]




'''