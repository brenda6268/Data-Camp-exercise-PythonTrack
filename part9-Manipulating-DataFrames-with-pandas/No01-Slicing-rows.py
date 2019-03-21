#Slicing rows
'''
The Pennsylvania US election results data set that you have been using so far is ordered by county name. This means that county names can be sliced alphabetically. In this exercise, you're going to perform slicing on the county names of the election DataFrame from the previous exercises, which has been pre-loaded for you.

Instructions
100 XP
Instructions
100 XP
Slice the row labels 'Perry' to 'Potter' and assign the output to p_counties.
Print the p_counties DataFrame. This has been done for you.
Slice the row labels 'Potter' to 'Perry' in reverse order. To do this for hypothetical row labels 'a' and 'b', you could use a stepsize of -1 like so: df.loc['b':'a':-1].
Print the p_counties_rev DataFrame. This has also been done for you, so hit 'Submit Answer' to see the result of your slicing!
'''

# Code
# Slice the row labels 'Perry' to 'Potter': p_counties
p_counties = election.loc['Perry':'Potter',:]   # my error: election.loc[['Perry':'Potter'],:]  
# Print the p_counties DataFrame
print(p_counties)

# Slice the row labels 'Potter' to 'Perry' in reverse order: p_counties_rev
#p_counties_rev = election.loc['Perry' : 'Potter':-1, :]

#p_counties_rev = election.loc['Perry' : 'Potter':-1] # my error: the order is verse.
p_counties_rev = election.loc['Potter':'Perry':-1]  
# Print the p_counties_rev DataFrame
print(p_counties_rev)

'''result

             state   total      Obama     Romney  winner   voters
county                                                           
Perry           PA   18240  29.769737  68.591009  Romney    27245
Philadelphia    PA  653598  85.224251  14.051451   Obama  1099197
Pike            PA   23164  43.904334  54.882576  Romney    41840
Potter          PA    7205  26.259542  72.158223  Romney    10913


             state   total      Obama     Romney  winner   voters
county                                                           
Potter          PA    7205  26.259542  72.158223  Romney    10913
Pike            PA   23164  43.904334  54.882576  Romney    41840
Philadelphia    PA  653598  85.224251  14.051451   Obama  1099197
Perry           PA   18240  29.769737  68.591009  Romney    27245

'''