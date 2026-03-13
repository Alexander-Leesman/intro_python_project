# Restarting the calculatepifunction.py

import numpy as np
import matplotlib.pyplot as plt
import random as rand
import math
from astropy.modeling import models, fitting

# Monte Carlo method: circle of radius r inside square with side length of 2r. Both are centered at the origin.
# n number of points plotted between 0 and r (this is a quarter of the square and a quarter of the circle)
# (points inside the quarter circle/n)*4 = approx. area of the circle
# approx. area / r**2 = approx. pi

def approximate_pi(radius = 1, n):     # radius of circle radius, number of points n
    # Approximation of the area of the circle via Monte Carlo
    points_inside = 0
    for ni in range(n):
        point = (rand.uniform(0,radius),rand.uniform(0,radius))
        if point[0]**2 + point[1]**2 <= radius**2:
            points_inside += 1
    # times 4 since the region is a quarter circle
    area = (points_inside/n)*4
    # approximate value of pi
    approximate_value_of_pi = area/(radius**2)
    return approximate_value_of_pi

# Reduced Chi squared to find the goodness of fit
# In this case, degrees of freedom = n-1
# Observed = fit line to the approximate values of pi
# parameter observed is a list/array
def reduced_chi_sq(observed):
    O = np.array(observed)
    E = math.pi
    # First, needs sample variance
    sample_variance = np.var(O, ddof=1)    # np array O, degrees of freedom = N - ddof     
    # Find the Chi-squared:
    chi_squared = np.sum(((O-E)**2)/(sample_variance))
    reduced_chi_squared = chi_squared/(len(O)-1)
    return reduced_chi_squared

# Find how the data converges
# For the convergence test, you find how many points it takes for it to stop changing (Within x percent of the last estimates)
# This should be made with the assumption that you do not know the true value. You want to see where it converges to.
# The question you are trying to answer: How many points do you need for you to confidently say that it has converged?
# Obviously, 10^15 points would be enough in this case, but that would take a while to compute.
# I guess the threshold percentage choice is up to me
# If for x amount of approximations the approximated values do not leave the threshold perentage of the previous value -> has converged

# INPUT: data (list/array), number of points (list/array); Will be used to approximate pi values
# OUTPUT : the number of points required for the data to converge
# takes a list/array of data, then checks if successive values have a 10% difference of eachother
# if 3 successive values are within said percentage, the function returns


def convergence_check(percent = 10, n = 1):
    p = percent/100
    n_value = n # approximate_pi will be calculated with 10**n_value points 
    pi_values = []
    pi_values.append(approximate_pi(1, 10**n_value))
    n_value += 1
    pi_values.append(approximate_pi(1, 10**n_value))
    n_value += 1
    while number_within < 2:
        pi_values.append(approximate_pi(1, 10**n_value))
        current_value = pi_values[-1]
        previous_value1 = pi_values[-2]
        previous_value2 = pi_values[-3]
        a = abs(previous_value2 - previous_value1)
        b = abs(previous_value1 - current_value)
        if a < (p * previous_value2):
            if b < (p * previous_value1):
                return 10**n_value
        n_value += 1