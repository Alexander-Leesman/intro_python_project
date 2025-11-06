#Line plotting function
#In: numpy arrays x, y, dy for x, y, and the uncertainty of y.
#Out: plot of x, y with uncertainty; prints slope and y-intercept to 2 decimal places.
#Needs these imports:
    #import numpy as np
    #import matplotlib.pyplot as plt
    #from astropy.modeling import models, fitting

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