# intro_python_project
For ASTR research intro Jupyter notebooks.  This is work I'm doing to acquaint myself with python and jupyter notebooks.

# Functions
## linefitfunction.py
### linefitfunction.fitline(x, y, dy)
Takes an array of x values, an array of their corresponding noisy y values, and the error of the y values
then plots them y vs. x, adds error bars for y, then uses astropy's models and fitting to plot a 1D linear fit to the data.

Parameters:\
&nbsp;x = array\
&nbsp;&nbsp;x coordinates\
&nbsp;y = array\
&nbsp;&nbsp;y coordinate\
&nbsp;dy = array\
&nbsp;&nbsp;error of y
    
Returns:\
&nbsp;plot of x vs scatter of y with error bars and plot of x vs LinearFit(x)\
&nbsp;&nbsp;LinearFit = object\
&nbsp;&nbsp;&nbsp;Linear fit of x vs. y\
&nbsp;prints string stating slope\
&nbsp;prints string stating y-intercept\
&nbsp;prints string of Chi Squared of LinearFit(x) compared to y\
&nbsp;prints string of Degrees of Freedom