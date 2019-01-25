#Creating a database engine
'''
Here, you're going to fire up your very first SQL engine. You'll create an engine to connect to the SQLite database 'Chinook.sqlite', which is in your working directory. Remember that to create an engine to connect to 'Northwind.sqlite', Hugo executed the command

engine = create_engine('sqlite:///Northwind.sqlite')
Here, 'sqlite:///Northwind.sqlite' is called the connection string to the SQLite database Northwind.sqlite. A little bit of background on the Chinook database: the Chinook database contains information about a semi-fictional digital media store in which media data is real and customer, employee and sales data has been manually created.

Why the name Chinook, you ask? According to their website,

#Instructions
100 XP
Import the function create_engine from the module sqlalchemy.
Create an engine to connect to the SQLite database 'Chinook.sqlite' and assign it to engine.
'''

# Code
# Import necessary module
from sqlalchemy import create_engine

# Create engine: engine
engine=create_engine('sqlite:///Chinook.sqlite')
