import numpy
import matplotlib.pyplot as plt

#import mysql.connector --> DB connector
#import pandas --> module to work with excel kind of files
#from sklearn import linear_model --> for predictions

speed = [52,32,55,98,78,41,35]
x=numpy.random.normal(0,45,100) # equal probability data
y=numpy.random.normal(50,10,100) # Normal distribution like bell curve. 50 is mean, 10 is SD.
standard_deviation = numpy.std(speed)
variance = numpy.var(speed)
#plt.hist(y,100) to show histogram
#plt.scatter(x,y) # to show X-Y axis plot


# generate polygraph

mymodel= numpy.poly1d(numpy.polyfit(x,y,2))
myline = numpy.linspace(-50,100,100)
plt.title("Simple Linear Regression")
plt.plot(myline,mymodel(myline))
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.scatter(x,y)
plt.legend
plt.show()