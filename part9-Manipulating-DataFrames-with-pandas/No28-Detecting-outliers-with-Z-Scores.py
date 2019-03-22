#Detecting outliers with Z-Scores
'''
As Dhavide demonstrated in the video using the zscore function, you can apply a .transform() method after grouping to apply a function to groups of data independently. The z-score is also useful to find outliers: a z-score value of +/- 3 is generally considered to be an outlier.

In this example, you're going to normalize the Gapminder data in 2010 for life expectancy and fertility by the z-score per region. Using boolean indexing, you will filter out countries that have high fertility rates and low life expectancy for their region.

The Gapminder DataFrame for 2010 indexed by 'Country' is provided for you as gapminder_2010.

Instructions
100 XP
Instructions
100 XP
Import zscore from scipy.stats.
Group gapminder_2010 by 'region' and transform the ['life','fertility'] columns by zscore.
Construct a boolean Series of the bitwise or between standardized['life'] < -3 and standardized['fertility'] > 3.
Filter gapminder_2010 using .loc[] and the outliers Boolean Series. Save the result as gm_outliers.
Print gm_outliers. This has been done for you, so hit 'Submit Answer' to see the results.
'''

# Code
# Import zscore
from scipy.stats import zscore

# Group gapminder_2010: standardized
standardized = gapminder_2010.groupby('region')[['life','fertility']].transform(zscore)

# Construct a Boolean Series to identify outliers: outliers
outliers = (standardized['life'] < -3) | (standardized['fertility'] > 3)

# Filter gapminder_2010 by the outliers: gm_outliers
gm_outliers = gapminder_2010.loc[outliers] #####

# Print gm_outliers
print(gm_outliers)

'''
             fertility    life  population  child_mortality     gdp                 region
Country                                                                                   
Guatemala        3.974  71.100  14388929.0             34.5  6849.0                America
Haiti            3.350  45.000   9993247.0            208.8  1518.0                America
Tajikistan       3.780  66.830   6878637.0             52.6  2110.0  Europe & Central Asia
Timor-Leste      6.237  65.952   1124355.0             63.8  1777.0    East Asia & Pacific


'''
'''
n [1]: gapminder_2010.head()
Out[1]: 
                     fertility    life  population  child_mortality      gdp                      region
Country                                                                                                 
Afghanistan              5.659  59.612  31411743.0            105.0   1637.0                  South Asia
Albania                  1.741  76.780   3204284.0             16.6   9374.0       Europe & Central Asia
Algeria                  2.817  70.615  35468208.0             27.4  12494.0  Middle East & North Africa
Angola                   6.218  50.689  19081912.0            182.5   7047.0          Sub-Saharan Africa
Antigua and Barbuda      2.130  75.437     88710.0              9.9  20567.0                     America


In [3]: standardized.head()
Out[3]: 
                         life  fertility
Country                                 
Afghanistan         -1.743601   2.504732
Albania              0.226367   0.010964
Algeria             -0.440196  -0.003972
Angola              -0.882537   1.095653
Antigua and Barbuda  0.240607  -0.363761


'''