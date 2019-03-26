#Merging to compute influence
'''
This exercise starts off with the DataFrames reshaped and hosts in the namespace.

Your task is to merge the two DataFrames and tidy the result.

The end result is a DataFrame summarizing the fractional change in the expanding mean of the percentage of medals won for the host country in each Olympic edition.

Instructions
100 XP

Merge reshaped and hosts using an inner join. Remember, how='inner' is the default behavior for pd.merge().
Print the first 5 rows of the DataFrame merged. This has been done for you. You should see that the rows are jumbled chronologically.
Set the index of merged to be 'Edition' and sort the index.
Print the first 5 rows of the DataFrame influence. This has been done for you, so hit 'Submit Answer' to see the results!
'''

 #Code
# Import pandas
import pandas as pd

# Merge reshaped and hosts: merged
merged = pd.merge(reshaped, hosts, how='inner')

# Print first 5 rows of merged
print(merged.head())

# Set Index of merged and sort it: influence
influence =  merged.set_index('Edition').sort_index()

# Print first 5 rows of influence
print(influence.head())

'''result
   Edition  NOC     Change
0     1956  AUS  54.615063
1     2000  AUS  12.554986
2     1920  BEL  54.757887
3     1976  CAN  -2.143977
4     2008  CHN  13.251332
         NOC      Change
Edition                 
1896     GRE         NaN
1900     FRA  198.002486
1904     USA  199.651245
1908     GBR  134.489218
1912     SWE   71.896226


'''