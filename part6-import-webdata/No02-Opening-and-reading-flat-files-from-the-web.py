#Opening and reading flat files from the web
'''

You have just imported a file from the web, saved it locally and loaded it into a DataFrame. If you just wanted to load a file from the web into a DataFrame without first saving it locally, you can do that easily using pandas. In particular, you can use the function pd.read_csv() with the URL as the first argument and the separator sep as the second argument.

The URL of the file, once again, is

'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'

# Instructions
100 XP

    Assign the URL of the file to the variable url.
    Read file into a DataFrame df using pd.read_csv(), recalling that the separator in the file is ';'.
    Print the head of the DataFrame df.
    Execute the rest of the code to plot histogram of the first feature in the DataFrame df
    '''

  # Code
  # Import packages
# Import packages
import matplotlib.pyplot as plt
import pandas as pd
from urllib.request import urlretrieve
# Assign url of file: url
url='https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'

#urlretrieve(url,'winequality-red.csv') this is saving localy
# Read file into a DataFrame: df
#df=pd.read_csv('winequality-red.csv',sep=';')
df=pd.read_csv(url,sep=';')#this is read out directly from url

# Print the head of the DataFrame
print(df.head())

# Plot first column of df
pd.DataFrame.hist(df.ix[:, 0:1])
plt.xlabel('fixed acidity (g(tartaric acid)/dm$^3$)')
plt.ylabel('count')
plt.show()

'''result
 fixed acidity  volatile acidity  citric acid  residual sugar  chlorides  \
0            7.4              0.70         0.00             1.9      0.076   
1            7.8              0.88         0.00             2.6      0.098   
2            7.8              0.76         0.04             2.3      0.092   
3           11.2              0.28         0.56             1.9      0.075   
4            7.4              0.70         0.00             1.9      0.076   

   free sulfur dioxide  total sulfur dioxide  density    pH  sulphates  \
0                 11.0                  34.0   0.9978  3.51       0.56   
1                 25.0                  67.0   0.9968  3.20       0.68   
2                 15.0                  54.0   0.9970  3.26       0.65   
3                 17.0                  60.0   0.9980  3.16       0.58   
4                 11.0                  34.0   0.9978  3.51       0.56   

   alcohol  quality  
0      9.4        5  
1      9.8        5  
2      9.8        5  
3      9.8        6  
4      9.4        5

'''


