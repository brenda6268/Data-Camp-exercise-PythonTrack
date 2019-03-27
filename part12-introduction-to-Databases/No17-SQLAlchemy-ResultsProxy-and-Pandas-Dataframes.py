#SQLAlchemy ResultsProxy and Pandas Dataframes
'''
We can feed a ResultProxy directly into a pandas DataFrame, which is the workhorse of many Data Scientists in PythonLand. Jason demonstrated this in the video. In this exercise, you'll follow exactly the same approach to convert a ResultProxy into a DataFrame.

Instructions

Import pandas as pd.
Create a DataFrame df using pd.DataFrame() on the ResultProxy results.
Set the columns of the DataFrame df.columns to be the columns from the first result object results[0].keys().
Print the DataFrame.
'''

# Code
# import pandas
import pandas as pd

# Create a DataFrame from the results: df
df = pd.DataFrame(results)

# Set column names
df.columns = results[0].keys()

# Print the Dataframe
print(df)

'''result

        state  population
0  California    36609002
1       Texas    24214127
2    New York    19465159
3     Florida    18257662
4    Illinois    12867077
'''