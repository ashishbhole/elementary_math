# to run: python3 scriptname.py
# This script computes the power series for sine function
# upto the given number of terms in the series and computes
# the l2 norm of error.

import os
import numpy as np
from matplotlib import pyplot as plt
import math

# The series will be computed for no of terms: 1, 2, 3, ... no_of_terms_in_series_max
no_of_terms_in_series_max = 30

x_min = 0.0
x_max = 2*np.pi
no_of_points = 100
x = np.linspace(x_min, x_max, no_of_points)

# closed form of the function
sinx_closed_form = np.sin(x)

# iteration over the no of terms in the series
for no_of_terms_in_series in range(no_of_terms_in_series_max):

   no_of_terms_in_series = no_of_terms_in_series + 1 

   # computing series
   sinx_series = np.zeros(no_of_points)
   for n in range(no_of_terms_in_series):
       sinx_series = sinx_series + ((-1)**n) * (x**(2*n+1)/math.factorial(2*n+1))

   # l2 norm of the error in function
   error = sinx_closed_form - sinx_series
   l2_error = np.sum(error**2)
   print('l2 norm of error in the series trucated after ', no_of_terms_in_series, ' terms = ', l2_error)

'''
   # visualizing the sine function, trucated series and error
   plt.figure(figsize=(10, 8))
   plt.subplot(211)
   plt.plot(x, sinx_closed_form, '-', x, sinx_series, '--')
   plt.legend(('closed form','series'))
   plt.title('sine function: closed from and the power truncated series upto %i terms' % no_of_terms_in_series)

   plt.subplot(212)
   plt.margins(0, 0.5) 
   plt.plot(x, error)
   plt.title('error in the closed form and the truncated power series upto %i terms' % no_of_terms_in_series)

   # uncomment below to visualize graphs
   plt.show()
'''
