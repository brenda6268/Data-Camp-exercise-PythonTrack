#Applying .drop_duplicates()
'''
What could be the difference between the 'Event_gender' and 'Gender' columns? You should be able to evaluate your guess by looking at the unique values of the pairs (Event_gender, Gender) in the data. In particular, you should not see something like (Event_gender='M', Gender='Women'). However, you will see that, strangely enough, there is an observation with (Event_gender='W', Gender='Men').

The duplicates can be dropped using the .drop_duplicates() method, leaving behind the unique observations. The DataFrame has been loaded as medals.

Instructions
100 XP
Select the columns 'Event_gender' and 'Gender'.
Create a dataframe ev_gen_uniques containing the unique pairs contained in ev_gen.
Print ev_gen_uniques. This has been done for you, so hit 'Submit Answer' to see the result.
'''

# Code
# Select columns: ev_gen
#ev_gen = medals['Event_gender','Gender']  #my error lost outside []
ev_gen = medals[['Event_gender','Gender']]  # same as :  medals.loc[:,['Event_gender','Gender']]
# Drop duplicate pairs: ev_gen_uniques
#ev_gen_uniques = medals.drop_duplicates(ev_gen)  #my error
ev_gen_uniques =ev_gen.drop_duplicates()
# Print ev_gen_uniques
print(ev_gen_uniques)

'''
  Event_gender Gender
0                M    Men
348              X    Men
416              W  Women
639              X  Women
23675            W    Men
'''

#my note: this way to choose the unique combine two columns.