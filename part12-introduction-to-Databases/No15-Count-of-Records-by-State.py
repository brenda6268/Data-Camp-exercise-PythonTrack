#Count of Records by State
'''
Often, we want to get a count for each record with a particular value in another column. The .group_by() method helps answer this type of query. You can pass a column to the .group_by() method and use in an aggregate function like sum() or count(). Much like the .order_by() method, .group_by() can take multiple columns as arguments.

Instructions

Import func from sqlalchemy.
Build a select statement to get the value of the state field and a count of the values in the age field, and store it as stmt.
Use the .group_by() method to group the statement by the state column.
Execute stmt using the connection to get the count and store the results as results.
Print the keys/column names of the results returned using results[0].keys().
'''

# Code
# Import func
from sqlalchemy import func

# Build a query to select the state and count of ages by state: stmt
stmt = select([census.columns.state, func.count(census.columns.age)])

# Group stmt by state
stmt = stmt.group_by(census.columns.state)

# Execute the statement and store all the records: results
results = connection.execute(stmt).fetchall()

# Print results
print(results)

# Print the keys/column names of the results returned
print(results[0].keys())  # [0] also can be other value.

'''result

[('Alabama', 172), ('Alaska', 172), ('Arizona', 172), ('Arkansas', 172), ('California', 172), ('Colorado', 172), ('Connecticut', 172), ('Delaware', 172), ('District of Columbia', 172), ('Florida', 172), ('Georgia', 172), ('Hawaii', 172), ('Idaho', 172), ('Illinois', 172), ('Indiana', 172), ('Iowa', 172), ('Kansas', 172), ('Kentucky', 172), ('Louisiana', 172), ('Maine', 172), ('Maryland', 172), ('Massachusetts', 172), ('Michigan', 172), ('Minnesota', 172), ('Mississippi', 172), ('Missouri', 172), ('Montana', 172), ('Nebraska', 172), ('Nevada', 172), ('New Hampshire', 172), ('New Jersey', 172), ('New Mexico', 172), ('New York', 172), ('North Carolina', 172), ('North Dakota', 172), ('Ohio', 172), ('Oklahoma', 172), ('Oregon', 172), ('Pennsylvania', 172), ('Rhode Island', 172), ('South Carolina', 172), ('South Dakota', 172), ('Tennessee', 172), ('Texas', 172), ('Utah', 172), ('Vermont', 172), ('Virginia', 172), ('Washington', 172), ('West Virginia', 172), ('Wisconsin', 172), ('Wyoming', 172)]

['state', 'count_1']

'''

'''
In [2]: results[0]
Out[2]: ('Alabama', 172)

In [3]: results[1].keys()
Out[3]: ['state', 'count_1']

'''