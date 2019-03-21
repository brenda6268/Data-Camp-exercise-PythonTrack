#Using .map() with a dictionary
'''
The .map() method is used to transform values according to a Python dictionary look-up. In this exercise you'll practice this method while returning to working with the election DataFrame, which has been pre-loaded for you.

Your job is to use a dictionary to map the values 'Obama' and 'Romney' in the 'winner' column to the values 'blue' and 'red', and assign the output to the new column 'color'.

Instructions
100 XP
Instructions
100 XP
Create a dictionary with the key:value pairs 'Obama':'blue' and 'Romney':'red'.
Use the .map() method on the 'winner' column using the red_vs_blue dictionary you created.
Print the output of election.head(). This has been done for you, so hit 'Submit Answer' to see the new column!
'''

# Code
# Create the dictionary: red_vs_blue
red_vs_blue = {'Obama':'blue', 'Romney':'red'}###the key is the element in 'winner' column

# Use the dictionary to map the 'winner' column to the new column: election['color']
election['color'] =election['winner'].map(red_vs_blue)######

# Print the output of election.head()
print(election.head())

'''result

          state   total      Obama     Romney  winner  voters color
county                                                             
Adams        PA   41973  35.482334  63.112001  Romney   61156   red
Allegheny    PA  614671  56.640219  42.185820   Obama  924351  blue
Armstrong    PA   28322  30.696985  67.901278  Romney   42147   red
Beaver       PA   80015  46.032619  52.637630  Romney  115157   red
Bedford      PA   21444  22.057452  76.986570  Romney   32189   red

'''