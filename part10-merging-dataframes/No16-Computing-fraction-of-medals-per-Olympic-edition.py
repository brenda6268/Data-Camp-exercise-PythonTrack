#Computing fraction of medals per Olympic edition
'''
In this exercise, you'll start with the DataFrames editions, medals, & medal_counts from prior exercises.

You can extract a Series with the total number of medals awarded in each Olympic edition.

The DataFrame medal_counts can be divided row-wise by the total number of medals awarded each edition; the method .divide() performs the broadcast as you require.

This gives you a normalized indication of each country's performance in each edition.

Instructions
100 XP
Set the index of the DataFrame editions to be 'Edition' (using the method .set_index()). Save the result as totals.
Extract the 'Grand Total' column from totals and assign the result back to totals.
Divide the DataFrame medal_counts by totals along each row. You will have to use the .divide() method with the option axis='rows'. Assign the result to fractions.
Print first & last 5 rows of the DataFrame fractions. This has been done for you, so hit 'Submit Answer' to see the results!
'''

# Code
# Set Index of editions: totals
totals = editions.set_index('Edition')

# Reassign totals['Grand Total']: totals
totals = totals['Grand Total']

# Divide medal_counts by totals: fractions
fractions = medal_counts.divide(totals, axis='rows')

# Print first & last 5 rows of fractions
print(fractions.head())
print(fractions.tail())

'''
NOC      AFG  AHO  ALG       ANZ  ARG  ARM       AUS       AUT  AZE  BAH  \
Edition                                                                    
1896     NaN  NaN  NaN       NaN  NaN  NaN  0.013245  0.033113  NaN  NaN   
1900     NaN  NaN  NaN       NaN  NaN  NaN  0.009766  0.011719  NaN  NaN   
1904     NaN  NaN  NaN       NaN  NaN  NaN       NaN  0.002128  NaN  NaN   
1908     NaN  NaN  NaN  0.023632  NaN  NaN       NaN  0.001244  NaN  NaN   
1912     NaN  NaN  NaN  0.011299  NaN  NaN       NaN  0.015819  NaN  NaN   

NOC        ...     URS  URU       USA  UZB  VEN  VIE  YUG  ZAM  ZIM       ZZX  
Edition    ...                                                                 
1896       ...     NaN  NaN  0.132450  NaN  NaN  NaN  NaN  NaN  NaN  0.039735  
1900       ...     NaN  NaN  0.107422  NaN  NaN  NaN  NaN  NaN  NaN  0.066406  
1904       ...     NaN  NaN  0.838298  NaN  NaN  NaN  NaN  NaN  NaN  0.017021  
1908       ...     NaN  NaN  0.078358  NaN  NaN  NaN  NaN  NaN  NaN       NaN  
1912       ...     NaN  NaN  0.114124  NaN  NaN  NaN  NaN  NaN  NaN       NaN  

[5 rows x 138 columns]
NOC          AFG  AHO       ALG  ANZ       ARG       ARM       AUS       AUT  \
Edition                                                                        
1992         NaN  NaN  0.001173  NaN  0.001173       NaN  0.033431  0.003519   
1996         NaN  NaN  0.001614  NaN  0.010758  0.001076  0.071006  0.001614   
2000         NaN  NaN  0.002481  NaN  0.009926  0.000496  0.090819  0.001985   
2004         NaN  NaN       NaN  NaN  0.023524       NaN  0.078579  0.004004   
2008     0.00049  NaN  0.000979  NaN  0.024976  0.002938  0.072968  0.001469   

NOC           AZE       BAH ...   URS       URU       USA       UZB       VEN  \
Edition                     ...                                                 
1992          NaN  0.000587 ...   NaN       NaN  0.131378       NaN       NaN   
1996     0.000538  0.002690 ...   NaN       NaN  0.139860  0.001076       NaN   
2000     0.001489  0.002978 ...   NaN  0.000496  0.123077  0.001985       NaN   
2004     0.002503  0.001001 ...   NaN       NaN  0.132132  0.002503  0.001001   
2008     0.003428  0.002449 ...   NaN       NaN  0.154261  0.002938  0.000490   

NOC           VIE       YUG       ZAM       ZIM  ZZX  
Edition                                               
1992          NaN       NaN       NaN       NaN  NaN  
1996          NaN  0.013986  0.000538       NaN  NaN  
2000     0.000496  0.012903       NaN       NaN  NaN  
2004          NaN       NaN       NaN  0.001502  NaN  
2008     0.000490       NaN       NaN  0.001959  NaN  

[5 rows x 138 columns]

'''
