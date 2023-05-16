# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 2021
@author: Dalia 
"""


from matplotlib import pyplot as plt
import numpy

#Rainfall in inches for set 1
set1 = [65.5574, 95.631, 77.9526, 85.4456, 69.6722, 86.5378, 86.233, 89.73819999999999,  84.7852,
            88.31580000000001, 84.86139999999999, 89.5858, 92.32900000000001, 90.9574, 87.24900000000001, 
            92.1512, 96.5708, 92.202, 85.3186, 80.1116, 85.4964, 96.3676, 93.82759999999999, 84.6582, 85.0392]
#Rainfall in inches for set 2
set2 = [25.81, 37.65, 30.69, 33.64, 27.43, 34.07, 33.95, 35.33, 33.38, 34.77, 33.41, 35.27, 36.35, 35.81,
        34.35, 36.28, 38.02, 36.30, 33.59, 31.54, 33.66, 37.94, 36.94, 33.33, 33.48]

#Locations, x-axis values
xs = ["Akron", "Albia", "Algona", "Allison", "Alton", "AmesW", "AmesSE", "Anamosa", "Ankeny", 
      "Atlantic", "Audubon", "Beaconsfield", "Bedford", "BellePlaine", "Bellevue", "Blockton",
      "Bloomfield", "Boone", "Brighton", "Britt", "Buckeye", "BurlingtonKBUR", "BurlingtonKBUR",
      "Carroll", ""]


#Compare data sets and show difference 
def mainPlot(set1, set2, xs):
    
    fig, ax = plt.subplots(1)
    
    #Calculate difference between set 1 and set 2 with new line
    diff = numpy.subtract(set1, set2)

    #Label each line and color
    plt.plot(xs, set1, 'g-', label='Before')
    plt.plot(xs, set2, 'r-', label='After') 
    plt.plot(xs, diff, 'b-', label = "Difference")
    
    #rotate names to make each visible
    plt.setp(ax.get_xticklabels(), rotation = 90)
    
    # center the legend and label each axis
    plt.legend(loc=9)
    plt.xlabel("Locations")
    plt.title("Rainfall Over 10 years (in inches)")
    plt.savefig("plot1.jpg")
    
    
#Create two seperate plots and label max and min  
def twoPlots(set1, set2, xs):
    
    fig, (ax1, ax2) = plt.subplots(1, 2)
    
    #Set axis and titles of each
    ax1.plot(xs, set1)
    ax1.set_title("Set 1: Before")
    ax2.plot(xs, set2)
    ax2.set_title("Set 2: After")
    
    #Rotate labels and change font size
    plt.setp(ax1.set_xticklabels(xs, rotation=90, fontsize = 5))
    plt.setp(ax2.set_xticklabels(xs, rotation=90, fontsize = 5))
    
    #min's
    ax1.plot(xs[0], set1[0], 'r*', label="Min")
    ax2.plot(xs[0], set2[0], 'r*', label="Min")
    #max's
    ax1.plot(xs[16], set1[16], 'g*', label="Max")
    ax2.plot(xs[16], set2[16], 'g*', label="Max")
    
    plt.legend(loc=4)
    plt.savefig("plot2.jpg")
    
    
#Create bar graph to levels of rainfall of sets
def barGraph(set1, set2, xs):
    
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    
    #create bar graph with data
    ax.bar(xs,set1, label="Before")
    ax.bar(xs, set2, label="After")
    plt.setp(ax.set_xticklabels(xs, rotation=90, fontsize = 5))
    
    #place legend in lower left and set title and axis label
    plt.legend(loc=3)
    plt.xlabel("Locations")
    plt.title("Rainfall Over 10 years (in inches)")
    plt.savefig("plot3.jpg")
    

def main():
     
    #Call functions
    mainPlot(set1, set2, xs)
    twoPlots(set1, set2, xs)
    barGraph(set1, set2, xs)
      
main()
