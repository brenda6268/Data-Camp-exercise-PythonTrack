#pandas hist, pdf and cdf
'''
Pandas relies on the .hist() method to not only generate histograms, but also plots of probability density functions (PDFs) and cumulative density functions (CDFs).

In this exercise, you will work with a dataset consisting of restaurant bills that includes the amount customers tipped.

The original dataset is provided by the Seaborn package.

Your job is to plot a PDF and CDF for the fraction column of the tips dataset. This column contains information about what fraction of the total bill is comprised of the tip.

Remember, when plotting the PDF, you need to specify normed=True in your call to .hist(), and when plotting the CDF, you need to specify cumulative=True in addition to normed=True.

All necessary modules have been imported and the tips dataset is available in the workspace as df. Also, some formatting code has been written so that the plots you generate will appear on separate rows.
#Instructions
100 XP
Plot a PDF for the values in fraction with 30 bins between 0 and 30%. The range has been taken care of for you. ax=axes[0] means that this plot will appear in the first row.
Plot a CDF for the values in fraction with 30 bins between 0 and 30%. Again, the range has been specified for you. To make the CDF appear on the second row, you need to specify ax=axes[1].
'''

# Code
# This formats the plots such that they appear on separate rows
fig, axes = plt.subplots(nrows=2, ncols=1)  
####https://blog.csdn.net/htuhxf/article/details/82986440#%E4%B8%80%E3%80%81fig%2C%20ax%20%3D%20plt.subplots()%E7%9A%84%E4%BD%9C%E7%94%A8%EF%BC%9F
#https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot

# Plot the PDF
df.fraction.plot(ax=axes[0], kind='hist', bins=30, normed=True, range=(0,.3))  #df.fraction.median()=0.15, so set range 0~0.3
plt.show()

# Plot the CDF
df.fraction.plot(ax=axes[1], kind='hist', bins=30,normed=True, cumulative=True,  range=(0,.3))
plt.show()