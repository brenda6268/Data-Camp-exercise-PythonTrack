#Combining columns of data
'''
Think of column-wise concatenation of data as stitching data together from the sides instead of the top and bottom. To perform this action, you use the same pd.concat() function, but this time with the keyword argument axis=1. The default, axis=0, is for a row-wise concatenation.

You'll return to the Ebola dataset you worked with briefly in the last chapter. It has been pre-loaded into a DataFrame called ebola_melt. In this DataFrame, the status and country of a patient is contained in a single column. This column has been parsed into a new DataFrame, status_country, where there are separate columns for status and country.

Explore the ebola_melt and status_country DataFrames in the IPython Shell. Your job is to concatenate them column-wise in order to obtain a final, clean DataFrame.

Instructions
100 XP

Concatenate ebola_melt and status_country column-wise into a single DataFrame called ebola_tidy. Be sure to specify axis=1 and to pass the two DataFrames in as a list.
Print the shape and then the head of the concatenated DataFrame, ebola_tidy.
'''

# Code
# Concatenate ebola_melt and status_country column-wise: ebola_tidy
ebola_tidy = pd.concat([ebola_melt,status_country],axis=1)

# Print the shape of ebola_tidy
print(ebola_tidy.shape)

# Print the head of ebola_tidy
print(ebola_tidy.head())


'''result
(1952, 6)
         Date  Day status_country  counts status country
0    1/5/2015  289   Cases_Guinea  2776.0  Cases  Guinea
1    1/4/2015  288   Cases_Guinea  2775.0  Cases  Guinea
2    1/3/2015  287   Cases_Guinea  2769.0  Cases  Guinea
3    1/2/2015  286   Cases_Guinea     NaN  Cases  Guinea
4  12/31/2014  284   Cases_Guinea  2730.0  Cases  Guinea

'''