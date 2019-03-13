#Further diagnosis
'''
In the previous exercise, you identified some potentially unclean or missing data. Now, you'll continue to diagnose your data with the very useful .info() method.

The .info() method provides important information about a DataFrame, such as the number of rows, number of columns, number of non-missing values in each column, and the data type stored in each column. This is the kind of information that will allow you to confirm whether the 'Initial Cost' and 'Total Est. Fee' columns are numeric or strings. From the results, you'll also be able to see whether or not all columns have complete data in them.

The full DataFrame df and the subset DataFrame df_subset have been pre-loaded. Your task is to use the .info() method on these and analyze the results.

Instructions
100 XP

Print the info of df.
Print the info of the subset dataframe, df_subset.
'''

# Code
# Print the info of df
print(df.info())

# Print the info of df_subset
print(df_subset.info())


'''result
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 12846 entries, 0 to 12845
Data columns (total 82 columns):
Job #                           12846 non-null int64
Doc #                           12846 non-null int64
Borough                         12846 non-null object
House #                         12846 non-null object
Street Name                     12846 non-null object
Block                           12846 non-null int64
Lot                             12846 non-null int64
Bin #                           12846 non-null int64
Job Type                        12846 non-null object
Job Status                      12846 non-null object
Job Status Descrp               12846 non-null object
Latest Action Date              12846 non-null object
Building Type                   12846 non-null object
Community - Board               12846 non-null object
Cluster                         0 non-null float64
Landmarked                      2067 non-null object
Adult Estab                     1 non-null object
Loft Board                      65 non-null object
City Owned                      1419 non-null object
Little e                        365 non-null object
PC Filed                        0 non-null float64
eFiling Filed                   12846 non-null object
Plumbing                        12846 non-null object
Mechanical                      12846 non-null object
Boiler                          12846 non-null object
Fuel Burning                    12846 non-null object
Fuel Storage                    12846 non-null object
Standpipe                       12846 non-null object
Sprinkler                       12846 non-null object
Fire Alarm                      12846 non-null object
Equipment                       12846 non-null object
Fire Suppression                12846 non-null object
Curb Cut                        12846 non-null object
Other                           12846 non-null object
Other Description               12846 non-null object
Applicant's First Name          12846 non-null object
Applicant's Last Name           12846 non-null object
Applicant Professional Title    12846 non-null object
Applicant License #             12846 non-null object
Professional Cert               6908 non-null object
Pre- Filing Date                12846 non-null object
Paid                            11961 non-null object
Fully Paid                      11963 non-null object
Assigned                        3817 non-null object
Approved                        4062 non-null object
Fully Permitted                 1495 non-null object
Initial Cost                    12846 non-null object
Total Est. Fee                  12846 non-null object
Fee Status                      12846 non-null object
Existing Zoning Sqft            12846 non-null int64
Proposed Zoning Sqft            12846 non-null int64
Horizontal Enlrgmt              231 non-null object
Vertical Enlrgmt                142 non-null object
Enlargement SQ Footage          12846 non-null int64
Street Frontage                 12846 non-null int64
ExistingNo. of Stories          12846 non-null int64
Proposed No. of Stories         12846 non-null int64
Existing Height                 12846 non-null int64
Proposed Height                 12846 non-null int64
Existing Dwelling Units         12846 non-null object
Proposed Dwelling Units         12846 non-null object
Existing Occupancy              12846 non-null object
Proposed Occupancy              12846 non-null object
Site Fill                       8641 non-null object
Zoning Dist1                    11263 non-null object
Zoning Dist2                    1652 non-null object
Zoning Dist3                    88 non-null object
Special District 1              3062 non-null object
Special District 2              848 non-null object
Owner Type                      0 non-null float64
Non-Profit                      971 non-null object
Owner's First Name              12846 non-null object
Owner's Last Name               12846 non-null object
Owner's Business Name           12846 non-null object
Owner's House Number            12846 non-null object
Owner'sHouse Street Name        12846 non-null object
City                            12846 non-null object
State                           12846 non-null object
Zip                             12846 non-null int64
Owner'sPhone #                  12846 non-null int64
Job Description                 12699 non-null object
DOBRunDate                      12846 non-null object
dtypes: float64(3), int64(15), object(64)
memory usage: 8.0+ MB
None
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 12846 entries, 0 to 12845
Data columns (total 13 columns):
Job #                      12846 non-null int64
Doc #                      12846 non-null int64
Borough                    12846 non-null object
Initial Cost               12846 non-null object
Total Est. Fee             12846 non-null object
Existing Zoning Sqft       12846 non-null int64
Proposed Zoning Sqft       12846 non-null int64
Enlargement SQ Footage     12846 non-null int64
Street Frontage            12846 non-null int64
ExistingNo. of Stories     12846 non-null int64
Proposed No. of Stories    12846 non-null int64
Existing Height            12846 non-null int64
Proposed Height            12846 non-null int64
dtypes: int64(10), object(3)
memory usage: 1.3+ MB
None

'''