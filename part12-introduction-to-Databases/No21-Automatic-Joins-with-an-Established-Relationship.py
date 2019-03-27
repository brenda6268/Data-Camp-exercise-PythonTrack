#Automatic Joins with an Established Relationship
'''
If you have two tables that already have an established relationship, you can automatically use that relationship by just adding the columns we want from each table to the select statement. Recall that Jason constructed the following query:

stmt = select([census.columns.pop2008, state_fact.columns.abbreviation])
in order to join the census and state_fact tables and select the pop2008 column from the first and the abbreviation column from the second. In this case, the census and state_fact tables had a pre-defined relationship: the state column of the former corresponded to the name column of the latter.

In this exercise, you'll use the same predefined relationship to select the pop2000 and abbreviation columns!

Instructions

Build a statement to join the census and state_fact tables and select the pop2000 column from the first and the abbreviation column from the second.
Execute the statement to get the first result and save it as result.
Hit 'Submit Answer' to loop over the keys of the result object, and print the key and value for each!
'''


# Code

# Build a statement to join census and state_fact tables: stmt
stmt = select([census.columns.pop2000, state_fact.columns.abbreviation])

# Execute the statement and get the first result: result
result = connection.execute(stmt).first()

# Loop over the keys in the result object and print the key and value
for key in result.keys():
    print(key, getattr(result, key))



'''result

pop2000 89600
abbreviation IL
'''

'''
In [2]: stmt1=select([census])

In [3]: result1=connection.execute(stmt1).fetchall()

In [5]: import pandas as pd

In [6]: df_census=pd.DataFrame(result1)

In [9]: df_census.columns=result1[0].keys()  # without this step, the column names are 0,1,2,...

In [10]: df_census.head()
Out[10]: 
      state sex  age  pop2000  pop2008
0  Illinois   M    0    89600    95012
1  Illinois   M    1    88445    91829
2  Illinois   M    2    88729    89547
3  Illinois   M    3    88868    90037
4  Illinois   M    4    91947    91111



In [16]: result0=connection.execute(stmt).fetchall()

In [17]: df=pd.DataFrame(result0)

In [18]: df.columns=result0[0].keys()

In [19]: df.head()
Out[19]: 
   pop2000 abbreviation
0    89600           IL
1    89600           NJ
2    89600           ND
3    89600           OR
4    89600           DC


In [20]: result
Out[20]: (89600, 'IL')   # because it only choose first()


In [21]: connection.execute(stmt)[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    connection.execute(stmt)[0]
TypeError: 'ResultProxy' object does not support indexing
'''