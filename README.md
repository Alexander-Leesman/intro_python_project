# intro_python_project
For ASTR research intro Jupyter notebooks.  This is work I'm doing to acquaint myself with python and jupyter notebooks.

# Functions
# linefitfunction.py
# linefitfunction.fitline(x, y, dy)
Takes an array of x values, an array of their corresponding noisy y values, and the error of the y values
then plots them y vs. x, adds error bars for y, then uses astropy's models and fitting to plot a 1D linear fit to the data.

Parameters:\
>x = array\
>>x coordinates\
>y = array\
>>y coordinate\
>dy = array\
>>error of y
    
Returns:\
    plot of x vs scatter of y with error bars and plot of x vs LinearFit(x)\
        LinearFit = object\
            Linear fit of x vs. y\
    prints string stating slope\
    prints string stating y-intercept\
    prints string of Chi Squared of LinearFit(x) compared to y\
    prints string of Degrees of Freedom