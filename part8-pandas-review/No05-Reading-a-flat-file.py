#Reading a flat file
'''
In previous exercises, we have preloaded the data for you using the pandas function read_csv(). Now, it's your turn! Your job is to read the World Bank population data you saw earlier into a DataFrame using read_csv(). The file is available in the variable data_file.

The next step is to reread the same file, but simultaneously rename the columns using the names keyword input parameter, set equal to a list of new column labels. You will also need to set header=0 to rename the column labels.

Finish up by inspecting the result with df.head() and df.info() in the IPython Shell (changing df to the name of your DataFrame variable).

pandas has already been imported and is available in the workspace as pd.

#Instructions
100 XP
Use pd.read_csv() with the string data_file to read the CSV file into a DataFrame and assign it to df1.
Create a list of new column labels - 'year', 'population' - and assign it to the variable new_labels.
Reread the same file, again using pd.read_csv(), but this time, add the keyword arguments header=0 and names=new_labels. Assign the resulting DataFrame to df2.
Print both the df1 and df2 DataFrames to see the change in column names. This has already been done for you.
'''

# Code
# Read in the file: df1
df1 = pd.read_csv(data_file)  # my error: data_file is a string, so do not need enclose it with ''

# Create a list of the new column labels: new_labels
new_labels =['year', 'population']

# Read in the file, specifying the header and names parameters: df2
df2 = pd.read_csv(data_file, header = 0, names = new_labels)

# Print both the DataFrames
print(df1)
print(df2)

'''result

   Year  Total Population
0  1960      3.034971e+09
1  1970      3.684823e+09
2  1980      4.436590e+09
3  1990      5.282716e+09
4  2000      6.115974e+09
5  2010      6.924283e+09


   year    population
0  1960  3.034971e+09
1  1970  3.684823e+09
2  1980  4.436590e+09
3  1990  5.282716e+09
4  2000  6.115974e+09
5  2010  6.924283e+09

'''

'''my note: if I set the header=None

[3]In
df3 = pd.read_csv(data_file, header = None, names = new_labels)

print(df3)


[4]Out

   year        population
0  Year  Total Population
1  1960      3034970564.0
2  1970      3684822701.0
3  1980      4436590356.0
4  1990      5282715991.0
5  2000      6115974486.0
6  2010      6924282937.0


'''