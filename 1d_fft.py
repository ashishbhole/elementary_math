# to run: python3 scriptname.py
# This is script demonstrates the use Fast Fourier transform.

import os
import numpy as np
from matplotlib import pyplot as plt
import math

# parameters
x_min = -1.0 ; x_max = 1.0

# parameters for Gaussian function
x_0   = 0.0 ; alp  = 100 ; beta = 50

# parameters for trigonamtric function
k1 = 50.0 ; k2 = 80.0
a1 = 1.0  ; a2 = 0.5

# iteration over the no of terms in the series
for N in range(6, 11):

   # No of sampling points should be 2**N for fft 
   no_of_points = 2**N

   dx  = (x_max-x_min) / float(no_of_points)
   x   = np.linspace(x_min, x_max, no_of_points)
   #fun = np.exp(-alp*(x-x_0)**2) * np.cos(beta*(x-x_0))
   fun = a1 * np.sin(2.0*np.pi*k1*x) + a2 * np.sin(2.0*np.pi*k2*x)

   fun_fft = np.fft.fft(fun)
   k       = np.linspace(0.0, 1.0/(2.0*dx), no_of_points//2)

   plt.figure(figsize=(8, 12))
   plt.subplot(211)
   plt.plot(x, fun, '-')
   plt.title('Function plotted with no of points = %i ' % no_of_points)
   plt.xlabel(r'$x$')
   plt.ylabel(r'$f(x)$')

   plt.subplot(212)
   plt.plot(k, 2.0/no_of_points * np.abs(fun_fft[0:no_of_points//2]), '-*')
   plt.title('FFT of the function plotted with no of points = %i ' % no_of_points)
   plt.xlabel('Wavenumber')
   plt.ylabel('Amplitude')  

   plt.subplots_adjust(hspace = 0.5)

   plt.show()
