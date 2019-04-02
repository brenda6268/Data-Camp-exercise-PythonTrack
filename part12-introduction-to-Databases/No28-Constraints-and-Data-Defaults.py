#Constraints and Data Defaults
'''
You're now going to practice creating a table with some constraints! Often, you'll need to make sure that a column is unique, nullable, a positive value, or related to a column in another table. This is where constraints come in.

As Jason showed you in the video, in addition to constraints, you can also set a default value for the column if no data is passed to it via the default keyword on the column.

Instructions

Table, Column, String, Integer, Float, Boolean are already imported from sqlalchemy.
Build a new table called data with a unique name (String), count (Integer) defaulted to 1, amount (Float), and valid (Boolean) defaulted to False.

Hit 'Submit Answer' to create the table in the database and to print the table details for data.
'''

# Code
from sqlalchemy import Table, Column, String, Integer, Float, Boolean

# Define a new table with a name, count, amount, and valid column: data
data = Table('data', metadata,
             Column('name', String(255), unique=True),
             Column('count', Integer(), default=1),
             Column('amount', Float()),
             Column('valid', Boolean(), default=False)
)

# Use the metadata to create the table
metadata.create_all(engine)

# Print the table details
print(repr(metadata.tables['data']))

'''result
Table('data', MetaData(bind=None), Column('name', String(length=255), table=<data>), Column('count', Integer(), table=<data>, default=ColumnDefault(1)), Column('amount', Float(), table=<data>), Column('valid', Boolean(), table=<data>, default=ColumnDefault(False)), schema=None)

'''

'''note
In [2]: data.constraints
Out[2]: 
{UniqueConstraint(Column('name', String(length=255), table=<data>)),
 PrimaryKeyConstraint(),
 CheckConstraint(<sqlalchemy.sql.elements.BinaryExpression object at 0x7fbd2402a908>, name='_unnamed_', table=Table('data', MetaData(bind=None), Column('name', String(length=255), table=<data>), Column('count', Integer(), table=<data>, default=ColumnDefault(1)), Column('amount', Float(), table=<data>), Column('valid', Boolean(), table=<data>, default=ColumnDefault(False)), schema=None), _create_rule=<sqlalchemy.util.langhelpers.portable_instancemethod object at 0x7fbd24027948>, _type_bound=True)}




'''