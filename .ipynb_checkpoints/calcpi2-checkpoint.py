# calculates pi using the Monte Carlo Method and an increasing number of random points (psudorandom generator)
# compares it to the value of math.pi
# Returns plot of approximate values vs number of points, linear fit of the approximations, and reduced chi squared value when compared to pi itself.
# This was created as a new function to preserve the old one

#Define a square region with sides of a certain length. In that region define a circle with a radius of your choosing.
#Monte Carlo Technique

import numpy as np
import matplotlib.pyplot as plt
import random as rand
import math

def calculatepi(x,n):
    #bounds of the square in both x and y directions
    a = 0
    b = x
    #circle of radius 5, centered at (0,0)
    # n = number of times looped
    pointsinside = 0
    for i in range(n):
        point = (rand.uniform(a,b),rand.uniform(a,b))
        if point[0]**2 + point[1]**2 <= x**2:
            pointsinside += 1
    #times 4 since the region is a quarter circle
    piapprox = (pointsinside/n)*4

    return piapprox

# list N is a list of n values; 10**N
# For the list N, the function calls calculatepi and finds an approximation of pi with n number of points and adds it to a list
# Simultaneously, a list with the same number of values is created, but all values are math.pi
# The reduced chi squared value between the approximate pi and math.pi is calculated, and they are both plotted vs. n
def plotpi(x, N):
    #First calculates an approximation of pi, then adds it to both a values list and a temporary list, then finds the average of values appended to the temporary list, then appends the average to a list of averages. 
    # The averages will be the approximate value of pi. The range of calculated data points will be the error. These will be plotted against the values of n.
    nopoints = [] # x values for all calculated values
    nopoints2 = [] # x values for the averages
    calcval = [] # calculated value from calculatepi function
    avgcalcval = [] # averages; the calculated value of pi at n
    pi = [] # the actual value of pi (math.pi); same length as avg
    standarderror = [] # Standard error of the average; used for the reduced chi squared.

    # starting value for number of points 10**h
    h = 0
    # number of times pi is calculated for each value of h = N
    k = 10
    rand.seed(1)
    while h <= N:
        av = [] # values of calculatepi appended here, then the values are averaged to find the approximate pi. It is then reset to an empty list for the next set of points.
        sampleavg = 0
        sstanddev = 0
        for l in range(k):   # Runs function calculatepi 10 times and finds average of those 10 values. May take a while to run.
            g = 10**h
            pic = calculatepi(x, g) # radius = x, number of points 10**g
            print(pic)
            nopoints.append(g)
            calcval.append(pic)
            av.append(pic)
            
        # find the Standard error.
        # First, find the standard deviation of the sample.
        top = 0
        sampleavg = sum(av)/k
        for value in range(len(av)):
            top  += (av[value]-sampleavg)**2
        sstanddev = (top/(k-1))**0.5
        #Then, divide it by the square root of the sample size to find the standard error.
        standerr = sstanddev / ((k)**0.5)
        standarderror.append(standerr)
        
        avgcalcval.append(sampleavg)
        nopoints2.append(10**h)
        pi.append(math.pi)
        h += 1

    print(avgcalcval, standarderror)

    # taken from the line fit function
     #Uses reduced chi squared to find goodness of fit.
    observ = avgcalcval
    expect = pi
    dy = standarderror
    chi = 0 
    for k in range(len(avgcalcval)):
        chi += ((observ[k] - expect[k])**2)/(dy[k]**2)
    chisquared = (chi)/(len(avgcalcval)-2)
    print(f'Chi Squared = {chisquared:3.2f}')
    print(f'Degrees of Freedom = {(len(avgcalcval)-2)}')

    
    


