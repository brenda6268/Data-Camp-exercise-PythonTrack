--Diagnosing problems using anti-join
/*
Another powerful join in SQL is the anti-join. It is particularly useful in identifying which records are causing an incorrect number of records to appear in join queries.

You will also see another example of a subquery here, as you saw in the first exercise on semi-joins. Your goal is to identify the currencies used in Oceanian countries!

Instructions 3/3
30 XP
Instructions 3/3
30 XP
Note that not all countries in Oceania were listed in the resulting inner join with currencies. Use an anti-join to determine which countries were not included!

Use NOT IN and (SELECT code FROM currencies) as a subquery to get the country code and country name for the Oceanian countries that are not included in the currencies table.
*/

SELECT countries.code, countries.name
FROM countries 
--INNER JOIN currencies AS c2
--ON countries.code = c2.code
WHERE countries.continent = 'Oceania'
    AND code NOT IN
        (SELECT code 
        From currencies
    )