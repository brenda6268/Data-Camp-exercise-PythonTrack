#Filter data selected from a Table - Simple
'''
Having connected to the database, it's now time to practice filtering your queries!

As mentioned in the video, a where() clause is used to filter the data that a statement returns. For example, to select all the records from the census table where the sex is Female (or 'F') we would do the following:

select([census]).where(census.columns.sex == 'F')

In addition to == we can use basically any python comparison operator (such as <=, !=, etc) in the where() clause.

Instructions

Select all records from the census table by passing in census as a list to select().
Append a where clause to stmt to return only the records with a state of 'New York'.
Execute the statement stmt using .execute() and retrieve the results using .fetchall().
Iterate over results and print the age, sex and pop2008 columns from each record. For example, you can print out the age of result with result.age.
'''

# Code
# Create a select query: stmt
stmt = select([census])

# Add a where clause to filter the results to only those for New York
stmt = stmt.where(census.columns.state == 'New York')

# Execute the query to retrieve all the data returned: results
results = connection.execute(stmt).fetchall()

#engine=create_engine('')
#connection=engine.connect()


# Loop over the results and print the age, sex, and pop2008
for result in results:
    print(result.age, result.sex, result.pop2008)


'''result
0 M 128088
1 M 125649
2 M 121615
3 M 120580

...
83 M 27217
84 M 23879
85 M 124478
0 F 122194
1 F 119661
2 F 116413
3 F 114877
...
81 F 50693
82 F 48206
83 F 47777
84 F 43454
85 F 273476

'''