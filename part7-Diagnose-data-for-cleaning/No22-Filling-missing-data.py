#Filling missing data
'''
Here, you'll return to the airquality dataset from Chapter 2. It has been pre-loaded into the DataFrame airquality, and it has missing values for you to practice filling in. Explore airquality in the IPython Shell to checkout which columns have missing values.

It's rare to have a (real-world) dataset without any missing values, and it's important to deal with them because certain calculations cannot handle missing values while some calculations will, by default, skip over any missing values.

Also, understanding how much missing data you have, and thinking about where it comes from is crucial to making unbiased interpretations of data.
#Instructions
100 XP
Calculate the mean of the Ozone column of airquality using the .mean() method on airquality.Ozone.
Use the .fillna() method to replace all the missing values in the Ozone column of airquality with the mean, oz_mean.
Hit 'Submit Answer' to see the result of filling in the missing values!
'''

# Code
# Calculate the mean of the Ozone column: oz_mean
oz_mean = airquality.Ozone.mean()

# Replace all the missing values in the Ozone column with the mean
airquality['Ozone'] = airquality['Ozone'].fillna(oz_mean)

# Print the info of airquality
print(airquality.info())
