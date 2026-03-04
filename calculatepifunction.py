# Restarting the calculatepifunction.py

# Monte Carlo method: circle of radius r inside square with side length of 2r. Both are centered at the origin.
# n number of points plotted between 0 and r (this is a quarter of the square and a quarter of the circle)
# (points inside the quarter circle/n)*4 = approx. area of the circle
# approx. area / r**2 = approx. pi

def approximatepi(radius, n):     # radius of circle radius, number of points n
    # Approximation of the area of the circle via Monte Carlo
    pointsinside = 0
    for i in range(n):
        point = (rand.uniform(0,radius),rand.uniform(0,radius))
        if point[0]**2 + point[1]**2 <= radius**2:
            pointsinside += 1
    #times 4 since the region is a quarter circle
    area = (pointsinside/n)*4
    
    


