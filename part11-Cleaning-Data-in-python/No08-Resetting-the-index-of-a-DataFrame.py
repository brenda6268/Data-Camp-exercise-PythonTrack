#Resetting the index of a DataFrame
'''
After pivoting airquality_melt in the previous exercise, you didn't quite get back the original DataFrame.

What you got back instead was a pandas DataFrame with a hierarchical index (also known as a MultiIndex).

Hierarchical indexes are covered in depth in Manipulating DataFrames with pandas. In essence, they allow you to group columns or rows by another variable - in this case, by 'Month' as well as 'Day'.

There's a very simple method you can use to get back the original DataFrame from the pivoted DataFrame: .reset_index(). Dan didn't show you how to use this method in the video, but you're now going to practice using it in this exercise to get back the original DataFrame from airquality_pivot, which has been pre-loaded.

Instructions
100 XP

Print the index of airquality_pivot by accessing its .index attribute. This has been done for you.
Reset the index of airquality_pivot using its .reset_index() method.
Print the new index of airquality_pivot.
Print the head of airquality_pivot.
'''

# Code
# Print the index of airquality_pivot
print(airquality_pivot.index)

# Reset the index of airquality_pivot: airquality_pivot_reset
airquality_pivot_reset = airquality_pivot.reset_index()

# Print the new index of airquality_pivot_reset
print(airquality_pivot_reset.index)

# Print the head of airquality_pivot_reset
print(airquality_pivot_reset.head())


'''result
MultiIndex(levels=[[5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]],
           labels=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]],
           names=['Month', 'Day'])
RangeIndex(start=0, stop=153, step=1)
measurement  Month  Day  Ozone  Solar.R  Temp  Wind
0                5    1   41.0    190.0  67.0   7.4
1                5    2   36.0    118.0  72.0   8.0
2                5    3   12.0    149.0  74.0  12.6
3                5    4   18.0    313.0  62.0  11.5
4                5    5    NaN      NaN  56.0  14.3

'''
'''compare the original dataframe:

In [4]: airquality
Out[4]: 
     Ozone  Solar.R  Wind  Temp  Month  Day
0     41.0    190.0   7.4    67      5    1
1     36.0    118.0   8.0    72      5    2
2     12.0    149.0  12.6    74      5    3
3     18.0    313.0  11.5    62      5    4
4      NaN      NaN  14.3    56      5    5
5     28.0      NaN  14.9    66      5    6
6     23.0    299.0   8.6    65      5    7
7     19.0     99.0  13.8    59      5    8
8      8.0     19.0  20.1    61      5    9
9      NaN    194.0   8.6    69      5   10
10     7.0      NaN   6.9    74      5   11
11    16.0    256.0   9.7    69      5   12
12    11.0    290.0   9.2    66      5   13
13    14.0    274.0  10.9    68      5   14
14    18.0     65.0  13.2    58      5   15
15    14.0    334.0  11.5    64      5   16
16    34.0    307.0  12.0    66      5   17
17     6.0     78.0  18.4    57      5   18
18    30.0    322.0  11.5    68      5   19
19    11.0     44.0   9.7    62      5   20
20     1.0      8.0   9.7    59      5   21
21    11.0    320.0  16.6    73      5   22
22     4.0     25.0   9.7    61      5   23
23    32.0     92.0  12.0    61      5   24
24     NaN     66.0  16.6    57      5   25
25     NaN    266.0  14.9    58      5   26
26     NaN      NaN   8.0    57      5   27
27    23.0     13.0  12.0    67      5   28
28    45.0    252.0  14.9    81      5   29
29   115.0    223.0   5.7    79      5   30
..     ...      ...   ...   ...    ...  ...
123   96.0    167.0   6.9    91      9    1
124   78.0    197.0   5.1    92      9    2
125   73.0    183.0   2.8    93      9    3
126   91.0    189.0   4.6    93      9    4
127   47.0     95.0   7.4    87      9    5
128   32.0     92.0  15.5    84      9    6
129   20.0    252.0  10.9    80      9    7
130   23.0    220.0  10.3    78      9    8
131   21.0    230.0  10.9    75      9    9
132   24.0    259.0   9.7    73      9   10
133   44.0    236.0  14.9    81      9   11
134   21.0    259.0  15.5    76      9   12
135   28.0    238.0   6.3    77      9   13
136    9.0     24.0  10.9    71      9   14
137   13.0    112.0  11.5    71      9   15
138   46.0    237.0   6.9    78      9   16
139   18.0    224.0  13.8    67      9   17
140   13.0     27.0  10.3    76      9   18
141   24.0    238.0  10.3    68      9   19
142   16.0    201.0   8.0    82      9   20
143   13.0    238.0  12.6    64      9   21
144   23.0     14.0   9.2    71      9   22
145   36.0    139.0  10.3    81      9   23
146    7.0     49.0  10.3    69      9   24
147   14.0     20.0  16.6    63      9   25
148   30.0    193.0   6.9    70      9   26
149    NaN    145.0  13.2    77      9   27
150   14.0    191.0  14.3    75      9   28
151   18.0    131.0   8.0    76      9   29
152   20.0    223.0  11.5    68      9   30

[153 rows x 6 columns]


'''