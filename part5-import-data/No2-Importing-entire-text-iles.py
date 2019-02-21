#Importing entire text files
#In this exercise, you'll be working with the file moby_dick.txt. It is a text file that contains the opening sentences of Moby Dick, one of the great American novels! Here you'll get experience opening a text file, printing its contents to the shell and, finally, closing it.


#Instructions

#Open the file moby_dick.txt as read-only and store it in the variable file. Make sure to pass the filename enclosed in quotation marks ''.
#Print the contents of the file to the shell using the print() function. As Hugo showed in the video, you'll need to apply the method read() to the object file.
#Check whether the file is closed by executing print(file.closed).
#Close the file using the close() method.
#Check again that the file is closed as you did above.


# Code

# Open a file: file
file = open('moby_dick.txt', mode='r')

# Print it
print(file.read())   # get the content of 'moby_dick.txt'

# Check whether file is closed
print(file.closed)   # output is bool 

# Close file
file.close()

# Check whether file is closed
print (file.closed)


''' result:
CHAPTER 1. Loomings.

Call me Ishmael. Some years ago--never mind how long precisely--having
little or no money in my purse, and nothing particular to interest me on
shore, I thought I would sail about a little and see the watery part of
the world. It is a way I have of driving off the spleen and regulating
the circulation. Whenever I find myself growing grim about the mouth;
whenever it is a damp, drizzly November in my soul; whenever I find
myself involuntarily pausing before coffin warehouses, and bringing up
the rear of every funeral I meet; and especially whenever my hypos get
such an upper hand of me, that it requires a strong moral principle to
prevent me from deliberately stepping into the street, and methodically
knocking people's hats off--then, I account it high time to get to sea
as soon as I can. This is my substitute for pistol and ball. With a
philosophical flourish Cato throws himself upon his sword; I quietly
take to the ship. There is nothing surprising in this. If they but knew
it, almost all men in their degree, some time or other, cherish very
nearly the same feelings towards the ocean with me.

False
True
'''
