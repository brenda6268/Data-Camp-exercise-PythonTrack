#Selecting data from a Table: raw SQL
'''
Using what we just learned about SQL and applying the .execute() method on our connection, we can leverage a raw SQL query to query all the records in our census table. The object returned by the .execute() method is a ResultProxy. On this ResultProxy, we can then use the .fetchall() method to get our results - that is, the ResultSet.

In this exercise, you'll use a traditional SQL query. In the next exercise, you'll move to SQLAlchemy and begin to understand its advantages. Go for it!

Instructions

Build a SQL statement to query all the columns from census and store it in stmt. Note that your SQL statement must be a string.
Use the .execute() and .fetchall() methods on connection and store the result in results. Remember that .execute() comes before .fetchall() and that stmt needs to be passed to .execute().
Print results.
'''

# Code
# Build select statement for census table: stmt
stmt = 'SELECT * FROM census'

# Execute the statement and fetch the results: results
results = connection.execute(stmt).fetchall()

# Print Results
print(results)#this is a list

'''result
[('Illinois', 'M', 0, 89600, 95012), ('Illinois', 'M', 1, 88445, 91829), ('Illinois', 'M', 2, 88729, 89547), ('Illinois', 'M', 3, 88868, 90037), ('Illinois', 'M', 4, 91947, 91111), ('Illinois', 'M', 5, 93894, 89802),...('Texas', 'F', 82, 33852, 41838), ('Texas', 'F', 83, 30076, 40489), ('Texas', 'F', 84, 27961, 36821), ('Texas', 'F', 85, 171538, 223439)]

In [2]: type(results)
Out[2]: list
'''