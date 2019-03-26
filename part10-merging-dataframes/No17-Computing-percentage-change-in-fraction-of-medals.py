#Computing percentage change in fraction of medals won
'''
Here, you'll start with the DataFrames editions, medals, medal_counts, & fractions from prior exercises.

To see if there is a host country advantage, you first want to see how the fraction of medals won changes from edition to edition.

The expanding mean provides a way to see this down each column. It is the value of the mean with all the data available up to that point in time. If you are interested in learning more about pandas' expanding transformations, this section of the pandas documentation has additional information.

Instructions
100 XP
Instructions
100 XP
Create mean_fractions by chaining the methods .expanding().mean() to fractions.
Compute the percentage change in mean_fractions down each column by applying .pct_change() and multiplying by 100. Assign the result to fractions_change.
Reset the index of fractions_change using the .reset_index() method. This will make 'Edition' an ordinary column.
Print the first and last 5 rows of the DataFrame fractions_change. This has been done for you, so hit 'Submit Answer' to see the results!
'''

# Code
# Apply the expanding mean: mean_fractions
mean_fractions = fractions.expanding().mean()

# Compute the percentage change: fractions_change
fractions_change = mean_fractions.pct_change()*100

# Reset the index of fractions_change: fractions_change
fractions_change = fractions_change.reset_index()

# Print first & last 5 rows of fractions_change
print(fractions_change.head())
print(fractions_change.tail())




''''
In [4]: fractions.head(20)
Out[4]: 
NOC      AFG  AHO       ALG       ANZ       ARG  ...  VIE       YUG       ZAM       ZIM       ZZX
Edition                                          ...                                             
1896     NaN  NaN       NaN       NaN       NaN  ...  NaN       NaN       NaN       NaN  0.039735
1900     NaN  NaN       NaN       NaN       NaN  ...  NaN       NaN       NaN       NaN  0.066406
1904     NaN  NaN       NaN       NaN       NaN  ...  NaN       NaN       NaN       NaN  0.017021
1908     NaN  NaN       NaN  0.023632       NaN  ...  NaN       NaN       NaN       NaN       NaN
1912     NaN  NaN       NaN  0.011299       NaN  ...  NaN       NaN       NaN       NaN       NaN
1920     NaN  NaN       NaN       NaN       NaN  ...  NaN       NaN       NaN       NaN       NaN
1924     NaN  NaN       NaN       NaN  0.012443  ...  NaN  0.002262       NaN       NaN       NaN
1928     NaN  NaN       NaN       NaN  0.045070  ...  NaN  0.016901       NaN       NaN       NaN
1932     NaN  NaN       NaN       NaN  0.006504  ...  NaN       NaN       NaN       NaN       NaN
1936     NaN  NaN       NaN       NaN  0.012571  ...  NaN  0.001143       NaN       NaN       NaN
1948     NaN  NaN       NaN       NaN  0.014742  ...  NaN  0.019656       NaN       NaN       NaN
1952     NaN  NaN       NaN       NaN  0.006749  ...  NaN  0.026997       NaN       NaN       NaN
1956     NaN  NaN       NaN       NaN  0.002260  ...  NaN  0.025989       NaN       NaN       NaN
1960     NaN  NaN       NaN       NaN  0.004535  ...  NaN  0.019274       NaN       NaN       NaN
1964     NaN  NaN       NaN       NaN  0.000990  ...  NaN  0.014851       NaN       NaN       NaN
1968     NaN  NaN       NaN       NaN  0.001940  ...  NaN  0.028128       NaN       NaN       NaN
1972     NaN  NaN       NaN       NaN  0.000844  ...  NaN  0.015190       NaN       NaN       NaN
1976     NaN  NaN       NaN       NaN       NaN  ...  NaN  0.014559       NaN       NaN       NaN
1980     NaN  NaN       NaN       NaN       NaN  ...  NaN  0.041096       NaN  0.011536       NaN
1984     NaN  NaN  0.001371       NaN       NaN  ...  NaN  0.059630  0.000685       NaN       NaN

[20 rows x 138 columns]

In [5]: mean_fractions.head(15)
Out[5]: 
NOC      AFG  AHO  ALG       ANZ       ARG  ...  VIE       YUG  ZAM  ZIM       ZZX
Edition                                     ...                                   
1896     NaN  NaN  NaN       NaN       NaN  ...  NaN       NaN  NaN  NaN  0.039735
1900     NaN  NaN  NaN       NaN       NaN  ...  NaN       NaN  NaN  NaN  0.053071
1904     NaN  NaN  NaN       NaN       NaN  ...  NaN       NaN  NaN  NaN  0.041054
1908     NaN  NaN  NaN  0.023632       NaN  ...  NaN       NaN  NaN  NaN  0.041054
1912     NaN  NaN  NaN  0.017466       NaN  ...  NaN       NaN  NaN  NaN  0.041054
1920     NaN  NaN  NaN  0.017466       NaN  ...  NaN       NaN  NaN  NaN  0.041054
1924     NaN  NaN  NaN  0.017466  0.012443  ...  NaN  0.002262  NaN  NaN  0.041054
1928     NaN  NaN  NaN  0.017466  0.028757  ...  NaN  0.009582  NaN  NaN  0.041054
1932     NaN  NaN  NaN  0.017466  0.021339  ...  NaN  0.009582  NaN  NaN  0.041054
1936     NaN  NaN  NaN  0.017466  0.019147  ...  NaN  0.006769  NaN  NaN  0.041054
1948     NaN  NaN  NaN  0.017466  0.018266  ...  NaN  0.009991  NaN  NaN  0.041054
1952     NaN  NaN  NaN  0.017466  0.016347  ...  NaN  0.013392  NaN  NaN  0.041054
1956     NaN  NaN  NaN  0.017466  0.014334  ...  NaN  0.015491  NaN  NaN  0.041054
1960     NaN  NaN  NaN  0.017466  0.013109  ...  NaN  0.016032  NaN  NaN  0.041054
1964     NaN  NaN  NaN  0.017466  0.011763  ...  NaN  0.015884  NaN  NaN  0.041054

[15 rows x 138 columns]


In [3]: fractions_change.head(20)
Out[3]: 
NOC      AFG  AHO  ALG        ANZ         ARG  ...  VIE         YUG  ZAM  ZIM        ZZX
Edition                                        ...                                      
1896     NaN  NaN  NaN        NaN         NaN  ...  NaN         NaN  NaN  NaN        NaN
1900     NaN  NaN  NaN        NaN         NaN  ...  NaN         NaN  NaN  NaN  33.561198
1904     NaN  NaN  NaN        NaN         NaN  ...  NaN         NaN  NaN  NaN -22.642384
1908     NaN  NaN  NaN        NaN         NaN  ...  NaN         NaN  NaN  NaN   0.000000
1912     NaN  NaN  NaN -26.092774         NaN  ...  NaN         NaN  NaN  NaN   0.000000
1920     NaN  NaN  NaN   0.000000         NaN  ...  NaN         NaN  NaN  NaN   0.000000
1924     NaN  NaN  NaN   0.000000         NaN  ...  NaN         NaN  NaN  NaN   0.000000
1928     NaN  NaN  NaN   0.000000  131.101152  ...  NaN  323.521127  NaN  NaN   0.000000
1932     NaN  NaN  NaN   0.000000  -25.794206  ...  NaN    0.000000  NaN  NaN   0.000000
1936     NaN  NaN  NaN   0.000000  -10.271982  ...  NaN  -29.357594  NaN  NaN   0.000000
1948     NaN  NaN  NaN   0.000000   -4.601500  ...  NaN   47.596769  NaN  NaN   0.000000
1952     NaN  NaN  NaN   0.000000  -10.508545  ...  NaN   34.043608  NaN  NaN   0.000000
1956     NaN  NaN  NaN   0.000000  -12.310760  ...  NaN   15.677209  NaN  NaN   0.000000
1960     NaN  NaN  NaN   0.000000   -8.545209  ...  NaN    3.488616  NaN  NaN   0.000000
1964     NaN  NaN  NaN   0.000000  -10.271938  ...  NaN   -0.920274  NaN  NaN   0.000000
1968     NaN  NaN  NaN   0.000000   -8.350855  ...  NaN    8.564598  NaN  NaN   0.000000
1972     NaN  NaN  NaN   0.000000   -8.379289  ...  NaN   -1.191550  NaN  NaN   0.000000
1976     NaN  NaN  NaN   0.000000    0.000000  ...  NaN   -1.323044  NaN  NaN   0.000000
1980     NaN  NaN  NaN   0.000000    0.000000  ...  NaN   12.034867  NaN  NaN   0.000000
1984     NaN  NaN  NaN   0.000000    0.000000  ...  NaN   16.657914  NaN  0.0   0.000000

[20 rows x 138 columns]

In [2]: fractions.index
Out[2]: Int64Index([1896, 1900, 1904, 1908, 1912, 1920, 1924, 1928, 1932, 1936, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008], dtype='int64', name='Edition')
 
 fractions_change = fractions_change.reset_index()


In [5]: fractions_change.head(20)
Out[5]: 
NOC  Edition  AFG  AHO  ALG        ANZ  ...  VIE         YUG  ZAM  ZIM        ZZX
0       1896  NaN  NaN  NaN        NaN  ...  NaN         NaN  NaN  NaN        NaN
1       1900  NaN  NaN  NaN        NaN  ...  NaN         NaN  NaN  NaN  33.561198
2       1904  NaN  NaN  NaN        NaN  ...  NaN         NaN  NaN  NaN -22.642384
3       1908  NaN  NaN  NaN        NaN  ...  NaN         NaN  NaN  NaN   0.000000
4       1912  NaN  NaN  NaN -26.092774  ...  NaN         NaN  NaN  NaN   0.000000
5       1920  NaN  NaN  NaN   0.000000  ...  NaN         NaN  NaN  NaN   0.000000
6       1924  NaN  NaN  NaN   0.000000  ...  NaN         NaN  NaN  NaN   0.000000
7       1928  NaN  NaN  NaN   0.000000  ...  NaN  323.521127  NaN  NaN   0.000000
8       1932  NaN  NaN  NaN   0.000000  ...  NaN    0.000000  NaN  NaN   0.000000
9       1936  NaN  NaN  NaN   0.000000  ...  NaN  -29.357594  NaN  NaN   0.000000
10      1948  NaN  NaN  NaN   0.000000  ...  NaN   47.596769  NaN  NaN   0.000000
11      1952  NaN  NaN  NaN   0.000000  ...  NaN   34.043608  NaN  NaN   0.000000
12      1956  NaN  NaN  NaN   0.000000  ...  NaN   15.677209  NaN  NaN   0.000000
13      1960  NaN  NaN  NaN   0.000000  ...  NaN    3.488616  NaN  NaN   0.000000
14      1964  NaN  NaN  NaN   0.000000  ...  NaN   -0.920274  NaN  NaN   0.000000
15      1968  NaN  NaN  NaN   0.000000  ...  NaN    8.564598  NaN  NaN   0.000000
16      1972  NaN  NaN  NaN   0.000000  ...  NaN   -1.191550  NaN  NaN   0.000000
17      1976  NaN  NaN  NaN   0.000000  ...  NaN   -1.323044  NaN  NaN   0.000000
18      1980  NaN  NaN  NaN   0.000000  ...  NaN   12.034867  NaN  NaN   0.000000
19      1984  NaN  NaN  NaN   0.000000  ...  NaN   16.657914  NaN  0.0   0.000000

[20 rows x 139 columns]

In [6]: fractions_change.index
Out[6]: RangeIndex(start=0, stop=26, step=1)

'''
'''
NOC  Edition  AFG  AHO  ALG        ANZ  ARG  ARM        AUS        AUT  AZE  \
0       1896  NaN  NaN  NaN        NaN  NaN  NaN        NaN        NaN  NaN   
1       1900  NaN  NaN  NaN        NaN  NaN  NaN -13.134766 -32.304688  NaN   
2       1904  NaN  NaN  NaN        NaN  NaN  NaN   0.000000 -30.169386  NaN   
3       1908  NaN  NaN  NaN        NaN  NaN  NaN   0.000000 -23.013510  NaN   
4       1912  NaN  NaN  NaN -26.092774  NaN  NaN   0.000000   6.254438  NaN   

NOC    ...      URS  URU         USA  UZB  VEN  VIE  YUG  ZAM  ZIM        ZZX  
0      ...      NaN  NaN         NaN  NaN  NaN  NaN  NaN  NaN  NaN        NaN  
1      ...      NaN  NaN   -9.448242  NaN  NaN  NaN  NaN  NaN  NaN  33.561198  
2      ...      NaN  NaN  199.651245  NaN  NaN  NaN  NaN  NaN  NaN -22.642384  
3      ...      NaN  NaN  -19.549222  NaN  NaN  NaN  NaN  NaN  NaN   0.000000  
4      ...      NaN  NaN  -12.105733  NaN  NaN  NaN  NaN  NaN  NaN   0.000000  

[5 rows x 139 columns]
NOC  Edition  AFG  AHO        ALG  ANZ       ARG        ARM        AUS  \
21      1992  NaN  0.0  -7.214076  0.0 -6.767308        NaN   2.754114   
22      1996  NaN  0.0   8.959211  0.0  1.306696        NaN  10.743275   
23      2000  NaN  0.0  19.762488  0.0  0.515190 -26.935484  12.554986   
24      2004  NaN  0.0   0.000000  0.0  9.625365   0.000000   8.161162   
25      2008  NaN  0.0  -8.197807  0.0  8.588555  91.266408   6.086870   

NOC       AUT        AZE ...   URS        URU       USA        UZB       VEN  \
21  -3.034840        NaN ...   0.0   0.000000 -1.329330        NaN  0.000000   
22  -3.876773        NaN ...   0.0   0.000000 -1.010378        NaN  0.000000   
23  -3.464221  88.387097 ...   0.0 -12.025323 -1.341842  42.258065  0.000000   
24  -2.186922  48.982144 ...   0.0   0.000000 -1.031922  21.170339 -1.615969   
25  -3.389836  31.764436 ...   0.0   0.000000 -0.450031  14.610625 -6.987342   

NOC       VIE       YUG        ZAM        ZIM  ZZX  
21        NaN  0.000000   0.000000   0.000000  0.0  
22        NaN -2.667732 -10.758472   0.000000  0.0  
23        NaN -2.696445   0.000000   0.000000  0.0  
24   0.000000  0.000000   0.000000 -43.491929  0.0  
25  -0.661117  0.000000   0.000000 -23.316533  0.0  

[5 rows x 139 columns]
'''