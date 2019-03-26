#Autoloading Tables from a Database
'''
SQLAlchemy can be used to automatically load tables from a database using something called reflection. Reflection is the process of reading the database and building the metadata based on that information. It's the opposite of creating a Table by hand and is very useful for working with existing databases. To perform reflection, you need to import the Table object from the SQLAlchemy package. Then, you use this Table object to read your table from the engine and autoload the columns. Using the Table object in this manner is a lot like passing arguments to a function. For example, to autoload the columns with the engine, you have to specify the keyword arguments autoload=True and autoload_with=engine to Table().

In this exercise, your job is to reflect the census table available on your engine into a variable called census. The metadata has already been loaded for you using MetaData() and is available in the variable metadata.

Instructions

Import the Table object from sqlalchemy.
Reflect the census table by using the Table object with the arguments:
The name of the table as a string ('census').
The metadata, contained in the variable metadata.
autoload=True
The engine to autoload with - in this case, engine.
Print the details of census using the repr() function.
'''

# Code
# Import Table
from sqlalchemy import Table

# Reflect census table from the engine: census
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Print census table metadata
print(repr(census))

'''result
Table('census', MetaData(bind=None), Column('state', VARCHAR(length=30), table=<census>), Column('sex', VARCHAR(length=1), table=<census>), Column('age', INTEGER(), table=<census>), Column('pop2000', INTEGER(), table=<census>), Column('pop2008', INTEGER(), table=<census>), schema=None)

'''

'''
# my note :repr__() is used to compute the “official” string representation of an object. 
The syntax of repr() method is:
     repr(obj)
 print string using repr() function then it prints with a pair of quotes and if we calculate
  a value we get more precise value than str() function.
'''