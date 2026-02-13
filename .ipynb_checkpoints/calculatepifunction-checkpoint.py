#Define a square region with sides of a certain length. In that region define a circle with a radius of your choosing.
#Monte Carlo Technique

import numpy as np
import matplotlib.pyplot as plt
import random as rand
import math
from astropy.modeling import models, fitting

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

# Finds an approximate value of pi by using calculatepi function several times.
# Plots and fits a line to the values.
# Finds Reduced Chi squared value of those values from math.pi
def plotpi(R, N):
    h =  10**N # number of points
    # Circle of radius R
    # Calculates an approximation of pi using calculatepi(R,h) 10 times
    X = []
    fX = []
    pi = []
    for j in range(10):
        X.append(j+1)
        pi.append(math.pi)
        fX.append(calculatepi(R, h))
    print("X = ",X,"fX = ", fX)



# Finds mean and sample variance of fX
    mean = sum(fX)/len(fX)
    print("mean = ",mean)
    top = 0
    for st in range(len(fX)):
        top += (fX[st]-mean)**2
    bottom = len(fX)-1
    sampleVariance = top/bottom
    print("Sample Variance = ",sampleVariance)

# Finds standard error
# standard error of the mean = sample standard deviation / sqrt(N)
    SE = []
    for se in range(len(fX)):
        SE.append(((sampleVariance)**0.5)/((len(fX))**0.5))
    print(SE)

# Finds reduced Chi Squared value
# chi squared = 1/len(fX) * ((sumation of (fXi - pi))**2/(sampleVariance))
# Comparing values to pi; no fit values
# reduced chi squared = chi squared / (len(fX) - 0)
    observ = fX
    expect = pi
    chis = 0 
    for k in range(len(fX)):
        chis += (observ[k] - expect[k])**2
    chisquared = (chis)/(sampleVariance)
    reducedChiSquared = chisquared/len(fX)
    
    #print(f'Chi Squared = {chisquared:3.2f}')
    print(f'Reduced Chi Squared = {reducedChiSquared:3.2f}')
    print(f'Degrees of Freedom = {(len(fX)-2)}')

    # Plots the list of calculated pi values as blue dots and the true value of pi as a black line.
    plt.plot(X, fX, 'b.', label = 'Approximations of π')
    plt.plot(X, pi, 'k-', label = 'π')
    plt.xlabel("x")
    plt.ylabel("Value Calculated")
    plt.errorbar(X, fX, yerr = SE, fmt = 'b.', label = 'Standard Error')
    plt.legend()
    plt.show()
