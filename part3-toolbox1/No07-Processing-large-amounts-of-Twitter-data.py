#Processing large amounts of Twitter data
'''
Sometimes, the data we have to process reaches a size that is too much for a computer's memory to handle. This is a common problem faced by data scientists. A solution to this is to process an entire data source chunk by chunk, instead of a single go all at once.

In this exercise, you will do just that. You will process a large csv file of Twitter data in the same way that you processed 'tweets.csv' in Bringing it all together exercises of the prequel course, but this time, working on it in chunks of 10 entries at a time.

If you are interested in learning how to access Twitter data so you can work with it on your own system, refer to Part 2 of the DataCamp course on Importing Data in Python.

The pandas package has been imported as pd and the file 'tweets.csv' is in your current directory for your use. Go for it!

Instructions
100 XP
Instructions
100 XP
Initialize an empty dictionary counts_dict for storing the results of processing the Twitter data.
Iterate over the 'tweets.csv' file by using a for loop. Use the loop variable chunk and iterate over the call to pd.read_csv() with a chunksize of 10.
In the inner loop, iterate over the column 'lang' in chunk by using a for loop. Use the loop variable entry.
'''
'''my note

the parameter 'chunksize=10' means the size of chunk, not the number of chunks. 

example: reference:https://blog.csdn.net/zm714981790/article/details/51375475 

In [138]: reader = pd.read_table('tmp.sv', sep='|', chunksize=4)

In [139]: reader
Out[139]: <pandas.io.parsers.TextFileReader at 0x120d2f290>

In [140]: for chunk in reader:
   .....:     print(chunk)
   .....: 
   Unnamed: 0         0         1         2         3
0           0  0.469112 -0.282863 -1.509059 -1.135632
1           1  1.212112 -0.173215  0.119209 -1.044236
2           2 -0.861849 -2.104569 -0.494929  1.071804
3           3  0.721555 -0.706771 -1.039575  0.271860
   Unnamed: 0         0         1         2         3
0           4 -0.424972  0.567020  0.276232 -1.087401
1           5 -0.673690  0.113648 -1.478427  0.524988
2           6  0.404705  0.577046 -1.715002 -1.039268
3           7 -0.370647 -1.157892 -1.344312  0.844885
   Unnamed: 0         0        1         2         3
0           8  1.075770 -0.10905  1.643563 -1.469388
1           9  0.357021 -0.67460 -1.776904 -0.968914
--------------------- 



If we know nothing about the big data, we can view few entries of data:

chunks = pd.read_csv('train.csv',iterator = True)   # set 'iterator = True' can get a TextFileReader
chunk = chunks.get_chunk(5)
print chunk
'''
'''
             date_time  site_name  posa_continent  user_location_country  \
0  2014-08-11 07:46:59          2               3                     66   
1  2014-08-11 08:22:12          2               3                     66   
2  2014-08-11 08:24:33          2               3                     66   
3  2014-08-09 18:05:16          2               3                     66   
4  2014-08-09 18:08:18          2               3                     66  
--------------------- 



'''


# Code
# Initialize an empty dictionary: counts_dict
counts_dict={}

# Iterate over the file chunk by chunk
for chunk in pd.read_csv('tweets.csv',chunksize=10):

    # Iterate over the column in DataFrame
    for entry in chunk['lang']:
        if entry in counts_dict.keys():
            counts_dict[entry] += 1
        else:
            counts_dict[entry] = 1

# Print the populated dictionary
print(counts_dict)
