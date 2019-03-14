#Iterating and concatenating all matches
'''
Now that you have a list of filenames to load, you can load all the files into a list of DataFrames that can then be concatenated.

You'll start with an empty list called frames. Your job is to use a for loop to:

iterate through each of the filenames
read each filename into a DataFrame, and then
append it to the frames list.
You can then concatenate this list of DataFrames using pd.concat(). Go for it!

Instructions
100 XP

Write a for loop to iterate through csv_files:
In each iteration of the loop, read csv into a DataFrame called df.
After creating df, append it to the list frames using the .append() method.
Concatenate frames into a single DataFrame called uber.
Hit 'Submit Answer' to see the head and shape of the concatenated DataFrame!
'''

#Code
# Create an empty list: frames
frames = []

#  Iterate over csv_files
for csv in csv_files:

    #  Read csv into a DataFrame: df
    df = pd.read_csv(csv)
    
    # Append df to frames
    frames.append(df)

# Concatenate frames into a single DataFrame: uber
uber = pd.concat(frames)

# Print the shape of uber
print(uber.shape)

# Print the head of uber
print(uber.head())


'''result
(297, 4)
          Date/Time      Lat      Lon    Base
0  5/1/2014 0:02:00  40.7521 -73.9914  B02512
1  5/1/2014 0:06:00  40.6965 -73.9715  B02512
2  5/1/2014 0:15:00  40.7464 -73.9838  B02512
3  5/1/2014 0:17:00  40.7463 -74.0011  B02512
4  5/1/2014 0:17:00  40.7594 -73.9734  B02512

'''