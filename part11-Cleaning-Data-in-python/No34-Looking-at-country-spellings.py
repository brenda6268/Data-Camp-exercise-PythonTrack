#Looking at country spellings
'''
Having tidied your DataFrame and checked the data types, your next task in the data cleaning process is to look at the 'country' column to see if there are any special or invalid characters you may need to deal with.

It is reasonable to assume that country names will contain:

The set of lower and upper case letters.
Whitespace between words.
Periods for any abbreviations.
To confirm that this is the case, you can leverage the power of regular expressions again. For common operations like this, Pandas has a built-in string method - str.contains() - which takes a regular expression pattern, and applies it to the Series, returning True if there is a match, and False otherwise.

Since here you want to find the values that do not match, you have to invert the boolean, which can be done using ~. This Boolean series can then be used to get the Series of countries that have invalid names.

Instructions
100 XP

Create a Series called countries consisting of the 'country' column of gapminder.
Drop all duplicates from countries using the .drop_duplicates() method.
Write a regular expression that tests your assumptions of what characters belong in countries:
Anchor the pattern to match exactly what you want by placing a ^ in the beginning and $ in the end.
Use A-Za-z to match the set of lower and upper case letters, \. to match periods, and \s to match whitespace between words.
Use str.contains() to create a Boolean vector representing values that match the pattern.
Invert the mask by placing a ~ before it.
Subset the countries series using the .loc[] accessor and mask_inverse. Then hit 'Submit Answer' to see the invalid country names!
'''

#Code

# Create the series of countries: countries
countries = gapminder.country

# Drop all the duplicates from countries
countries = countries.drop_duplicates()

# Write the regular expression: pattern
pattern = '^[A-Za-z\.\s]*$'

#Use A-Za-z to match the set of lower and upper case letters, 
#\. to match periods, 
#and \s to match whitespace between words.

# Create the Boolean vector: mask
mask = countries.str.contains(pattern)

# Invert the mask: mask_inverse
mask_inverse = ~countries.str.contains(pattern)

# Subset countries using mask_inverse: invalid_countries
invalid_countries = countries.loc[mask_inverse]

# Print invalid_countries
print(invalid_countries)



'''result
49            Congo, Dem. Rep.
50                 Congo, Rep.
53               Cote d'Ivoire
73      Falkland Is (Malvinas)
93               Guinea-Bissau
98            Hong Kong, China
118    United Korea (former)\n
131               Macao, China
132             Macedonia, FYR
145      Micronesia, Fed. Sts.
161            Ngorno-Karabakh
187             St. Barthélemy
193     St.-Pierre-et-Miquelon
225                Timor-Leste
251      Virgin Islands (U.S.)
252       North Yemen (former)
253       South Yemen (former)
258                      Åland
Name: country, dtype: object

'''

