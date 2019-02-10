--Union2
/*
UNION can also be used to determine all occurrences of a field across multiple tables. Try out this exercise with no starter code.

Instructions
100 XP
Determine all (non-duplicated) country codes in either the cities or the currencies table. The result should be a table with only one field called country_code.
Sort by country_code in alphabetical order.

*/

SELECT country_code   --this column name will show in the result table
FROM cities 
UNION
SELECT code           --this column name won't show in the result table
FROM currencies
ORDER BY country_code    --order should put behind the end of UNION tables
