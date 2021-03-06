#Filtering columns using other columns
'''
The election results DataFrame has a column labeled 'margin' which expresses the number of extra votes the winner received over the losing candidate. This number is given as a percentage of the total votes cast. It is reasonable to assume that in counties where this margin was less than 1%, the results would be too-close-to-call.

Your job is to use boolean selection to filter the rows where the margin was less than 1. You'll then convert these rows of the 'winner' column to np.nan to indicate that these results are too close to declare a winner.

The DataFrame has been pre-loaded for you as election.

Instructions
100 XP
Instructions
100 XP
Import numpy as np.
Create a boolean array for the condition where the 'margin' column is less than 1 and assign it to too_close.
Convert the entries in the 'winner' column where the result was too close to call to np.nan.
Print the output of election.info(). This has been done for you, so hit 'Submit Answer' to see the results.
'''
# Code
# Import numpy
import numpy as np

# Create the boolean array: too_close
too_close = election['margin']<1

# Assign np.nan to the 'winner' column where the results were too close to call
election.loc[too_close,'winner'] = np.nan

# Print the output of election.info()
print(election.info())


'''result
<class 'pandas.core.frame.DataFrame'>
Index: 67 entries, Adams to York
Data columns (total 8 columns):
state      67 non-null object
total      67 non-null int64
Obama      67 non-null float64
Romney     67 non-null float64
winner     64 non-null object
voters     67 non-null int64
turnout    67 non-null float64
margin     67 non-null float64
dtypes: float64(4), int64(2), object(2)
memory usage: 4.7+ KB
None

''