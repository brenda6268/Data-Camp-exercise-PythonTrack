#Reading multiple files to build a DataFrame
'''
It is often convenient to build a large DataFrame by parsing many files as DataFrames and concatenating them all at once. You'll do this here with three files, but, in principle, this approach can be used to combine data from dozens or hundreds of files.

Here, you'll work with DataFrames compiled from The Guardian's Olympic medal dataset.

pandas has been imported as pd and two lists have been pre-loaded: An empty list called medals, and medal_types, which contains the strings 'bronze', 'silver', and 'gold'.

Instructions
100 XP
Instructions
100 XP
Iterate over medal_types in the for loop.
Inside the for loop:
Create file_name using string interpolation with the loop variable medal. This has been done for you. The expression "%s_top5.csv" % medal evaluates as a string with the value of medal replacing %s in the format string.
Create the list of column names called columns. This has been done for you.
Read file_name into a DataFrame called medal_df. Specify the keyword arguments header=0, index_col='Country', and names=columns to get the correct row and column Indexes.
Append medal_df to medals using the list .append() method.
Concatenate the list of DataFrames medals horizontally (using axis='columns') to create a single DataFrame called medals. Print it in its entirety.
'''

# Code

for medal in medal_types:

    # Create the file name: file_name
    file_name = "%s_top5.csv" % medal
    
    # Create list of column names: columns
    columns = ['Country', medal]
    
    # Read file_name into a DataFrame: df
    medal_df = pd.read_csv(file_name, header=0, index_col='Country', names=columns)

    # Append medal_df to medals
    medals.append(medal_df)  #medals is a list here
    #In [5]: len(medals)
    #Out[5]: 3

# Concatenate medals horizontally: medals
medals = pd.concat(medals,axis='columns')  #medal is a dataframe here
#In [8]: type(medals)
#Out[8]: pandas.core.frame.DataFrame

# Print medals
print(medals)

'''
bronze  silver    gold
France           475.0   461.0     NaN
Germany          454.0     NaN   407.0
Italy              NaN   394.0   460.0
Soviet Union     584.0   627.0   838.0
United Kingdom   505.0   591.0   498.0
United States   1052.0  1195.0  2088.0
'''

'''
In [4]: medal_types
Out[4]: ['bronze', 'silver', 'gold']

In [5]: file_name
Out[5]: 'gold_top5.csv'

'''