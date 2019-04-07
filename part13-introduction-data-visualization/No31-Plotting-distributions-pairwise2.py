#Plotting distributions pairwise (2)
'''
In this exercise, you will generate pairwise joint distributions again. This time, you will make two particular additions:

You will display regressions as well as scatter plots in the off-diagonal subplots. You will do this with the argument kind='reg' (where 'reg' means 'regression'). Another option for kind is 'scatter' (the default) that plots scatter plots in the off-diagonal subplots.
You will also visualize the joint distributions separated by continent of origin. You will do this with the keyword argument hue specifying the 'origin'.

Instructions
100 XP
Plot the pairwise joint distributions separated by continent of origin and display the regressions.
'''

# Code
# Print the first 5 rows of the DataFrame
print(auto.head())

# Plot the pairwise joint distributions grouped by 'origin' along with regression lines
sns.pairplot(auto, hue='origin', kind='reg')
# Display the plot
plt.show()


'''result

    mpg   hp  origin
0  18.0   88      US
1   9.0  193      US
2  36.1   60    Asia
3  18.5   98      US
4  34.3   78  Europe

'''