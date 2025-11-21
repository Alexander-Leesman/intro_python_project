#Define a square region with sides of a certain length. In that region define a circle with a radius of your choosing.
#Monte Carlo Technique

def calculatepi(x):
    #bounds of the square in both x and y directions
    a = 0
    b = x
    #circle of radius 5, centered at (0,0)

    n = 10000000
    pointsinside = 0
    for i in range(n):
        point = (rand.uniform(a,b),rand.uniform(a,b))
        if point[0]**2 + point[1]**2 <= x**2:
            pointsinside += 1
    #times 4 since the region is a quarter circle
    piapprox = (pointsinside/n)*4

    return piapprox