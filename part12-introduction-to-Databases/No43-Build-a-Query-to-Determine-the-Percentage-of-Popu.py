#Build a Query to Determine the Percentage of Population by Gender and State
'''
In this exercise, you will write a query to determine the percentage of the population in 2000 that comprised of women. You will group this query by state.

Instructions

Import case, cast and Float from sqlalchemy.
Define a statement to select state and the percentage of females in 2000.
Inside func.sum(), use case() to select females (using the sex column) from pop2000. Remember to specify else_=0 if the sex is not 'F'.
To get the percentage, divide the number of females in the year 2000 by the overall population in 2000. Cast the divisor - census.columns.pop2000 - to Float before multiplying by 100.
Group the query by state.
Execute the query and store it as results.
Print state and percent_female for each record. This has been done for you, so hit 'Submit Answer' to see the result.
'''

# Code

# import case, cast and Float from sqlalchemy
from sqlalchemy import case, cast, Float

# Build a query to calculate the percentage of females in 2000: stmt
stmt = select([census.columns.state,
    (func.sum(
        case([
            (census.columns.sex == 'F', census.columns.pop2000)
        ], else_=0)) /
     cast(func.sum(census.columns.pop2000), Float) * 100).label('percent_female')
])

# Group By state
stmt = stmt.group_by(census.columns.state)

# Execute the query and store the results: results
results = connection.execute(stmt).fetchall()

# Print the percentage
for result in results:
    print(result.state, result.percent_female)

 '''result

Alabama 51.8324077702
Alaska 49.3014978935
Arizona 50.2236130306
Arkansas 51.2699284622
California 50.3523321490
Colorado 49.8476706030
Connecticut 51.6681650713
Delaware 51.6110973356
District of Columbia 53.1296261417
Florida 51.3648800117
Georgia 51.1140835034
Hawaii 51.1180118369
Idaho 49.9897262390
Illinois 51.1122423480
Indiana 50.9548031330
Iowa 50.9503983425
Kansas 50.8218641078
Kentucky 51.3268703693
Louisiana 51.7535159655
Maine 51.5057081342
Maryland 51.9357554997
Massachusetts 51.8430235713
Michigan 50.9724651832
Minnesota 50.4933294430
Mississippi 51.9222948179
Missouri 51.4688860264
Montana 50.3220269073
Nebraska 50.8584549336
Nevada 49.3673636138
New Hampshire 50.8580198450
New Jersey 51.5171395613
New Mexico 51.0471720798
New York 51.8345386515
North Carolina 51.4822623221
North Dakota 50.5006936323
Ohio 51.4655035002
Oklahoma 51.1136245708
Oregon 50.4294670362
Pennsylvania 51.7404347305
Rhode Island 52.0734339190
South Carolina 51.7307212977
South Dakota 50.5258358137
Tennessee 51.4306896994
Texas 50.5157216642
Utah 49.9729527511
Vermont 51.0185732099
Virginia 51.6572524472
Washington 50.5185650872
West Virginia 51.4004231809
Wisconsin 50.6148645265
Wyoming 49.9459554265

 '''