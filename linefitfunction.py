#Line plotting function
#In: numpy arrays x, y, dy for x, y, and the uncertainty of y.
#Out: plot of x, y with uncertainty; prints slope and y-intercept to 2 decimal places.
#Needs these imports:
    #import numpy as np
    #import matplotlib.pyplot as plt
    #from astropy.modeling import models, fitting

import numpy as np
from astropy.io import ascii
from astropy.table import Table
import matplotlib.pyplot as plt
from astropy.modeling import models, fitting


#Use chi squared
#Find reduced chi squared.

def fitline(x,y,dy):
    #Class 
    Fitter = fitting.LinearLSQFitter()
    initLine = models.Linear1D()
    #Object
    #Linear fit, with uncertainty dy
    LinearFit = Fitter(initLine, x,y)
    #Plots linear fit using matplotlib
    #Black dots are data, black line is the linear fit.
    plt.plot(x,LinearFit(x), 'k-', label='Linear Fit')
    plt.errorbar(x, y, yerr = dy, fmt = 'ko', label = 'Data')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()
    print(f'slope = {LinearFit.slope.value:3.2f}')
    print(f'intercept = {LinearFit.intercept.value:3.2f}')

    #Uses reduced chi squared to find goodness of fit.
    observ = y
    expect = LinearFit(x)
    chi = 0 
    for i in range(len(y)):
        chi += ((observ[i] - expect[i])**2)/(dy[i]**2)
    chisquared = (chi)/(len(y)-2)
    print(f'Chi Squared = {chisquared:3.2f}')
    print(f'Degrees of Freedom = {(len(y)-2)}')