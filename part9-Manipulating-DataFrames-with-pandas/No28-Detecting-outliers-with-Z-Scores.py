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
gm_outliers = gapminder_2010.loc[outliers]

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