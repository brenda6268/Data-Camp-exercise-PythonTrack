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