#Working on Blocks of Records
'''
Fantastic work so far! As Jason discussed in the video, sometimes you may have the need to work on a large ResultProxy, and you may not have the memory to load all the results at once. To work around that issue, you can get blocks of rows from the ResultProxy by using the .fetchmany() method inside a loop. With .fetchmany(), give it an argument of the number of records you want. When you reach an empty list, there are no more rows left to fetch, and you have processed all the results of the query. Then you need to use the .close() method to close out the connection to the database.

You'll now have the chance to practice this on a large ResultProxy called results_proxy that has been pre-loaded for you to work with.

Instructions

Use a while loop that checks if there are more_results.
Inside the loop, apply the method .fetchmany() to results_proxy to get 50 records at a time and store those records as partial_results.
After fetching the records, if partial_results is an empty list (that is, if it is equal to []), set more_results to False.
Loop over the partial_results and, if row.state is a key in the state_count dictionary, increment state_count[row.state] by 1; otherwise set state_count[row.state] to 1.
After the while loop, close the ResultProxy results_proxy using .close().
Hit 'Submit Answer' to print state_count.
'''

# Code
# Start a while loop checking for more results
# init more_results = True
# init state_count = {}

while more_results:
    # Fetch the first 50 results from the ResultProxy: partial_results  fetchone())  # fetch the first row only
    partial_results = results_proxy.fetchmany(50)

    # if empty list, set more_results to False
    if partial_results == []:
        more_results = False

    # Loop over the fetched records and increment the count for the state
    for row in partial_results:
        if row.state in state_count:
            state_count[row.state] += 1
        else:
            state_count[row.state] = 1

# Close the ResultProxy, and thus the connection
results_proxy.close()    # this line is not belong to while loop. so after finish while loop, will execute close

# Print the count by state
print(state_count)

'''result
{'New Jersey': 172, 'Massachusetts': 16, 'Idaho': 172, 'Florida': 172, 'District of Columbia': 172, 'North Dakota': 75, 'Maryland': 49, 'Illinois': 172}

'''

'''mynote
When used in write mode, calling fetchmany(n) will position the record pointer at case n of the active dataset. 
In the case that the dataset has splits and n is greater than the number of remaining cases in the current split, 
fetchmany(n) will position the record pointer at the end of the current split.

ref:https://www.ibm.com/support/knowledgecenter/en/SSLVMB_22.0.0/com.ibm.spss.statistics.python.help/spss/programmability_option/python_package_cursor_methods_fetchmany.htm


'''