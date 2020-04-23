# to run: python3 scriptname.py
# This is script plots exact solution of 1D advection equation and its fft.

import os
import numpy as np
from matplotlib import pyplot as plt
import math
from matplotlib import gridspec

# parameters
x_min = -1.0 ; x_max = 1.0 ; no_of_points = 1024
t_final = 0.75
dx  = (x_max-x_min) / float(no_of_points)
x   = np.linspace(x_min, x_max, no_of_points)

# parameters for Gaussian function
x_0   = -0.5 ; alp  = 100 ; beta = 50

# funtion and its fft
c = 1.0
fun = np.exp(-alp*(x-x_0)**2) * np.cos(beta*(x-x_0))
fun_fft = np.fft.fft(fun)
k       = np.linspace(0.0, 1.0/(2.0*dx), no_of_points//2)

# figure configuration
plt.ion()
fig2  = plt.figure(figsize=(10, 6))
gs2   = gridspec.GridSpec(ncols=1, nrows=2, hspace=0.3)

# Plot 1D wave propagation. A comma is needed to update the variable.
ax1  = plt.subplot(gs2[0])
up1,= ax1.plot(x,fun)
ax1.set_xlim(x_min, x_max)
ax1.set_ylim(np.min(fun)-0.1, np.max(fun)+1.1)
ax1.set_title('Exact solution of 1D advection equation at t = %f ' % t)
ax1.set_xlabel(r'$x$')
ax1.set_ylabel(r'$f(x)$')

# plot fft
ax2  = plt.subplot(gs2[1])
up2,= ax2.plot(k, 2.0/no_of_points * np.abs(fun_fft[0:no_of_points//2]), '-*') 
ax2.set_title('FFT of the function at time t = %f ' % t)
ax2.set_xlabel('Wavenumber')
ax2.set_ylabel('Amplitude')

plt.show()

# Exact solution and its fft
n_frames = 200
dt = t_final/float(n_frames)
t = 0
for it in range(n_frames):
   t = t + dt 
   fun = np.exp(-alp*(x-c*t-x_0)**2) * np.cos(beta*(x-c*t-x_0))
   fun_fft = np.fft.fft(fun)
   ax1.set_title('Exact solution of 1D advection equation at t = %f ' % t)
   up1.set_ydata(fun)
   ax2.set_title('FFT of the function at time t = %f ' % t)   
   up2.set_ydata(2.0/no_of_points * np.abs(fun_fft[0:no_of_points//2]))
   plt.gcf().canvas.draw()
