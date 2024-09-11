# %% Cell 1
import numpy as np
import matplotlib.pyplot as plt
#%% Cell 2
mo = 1500
u = 6000
vo = 200 #m/s
g = 9.8
y0 = 1000 #m
t = np.arange(0,int(1000/10))

def v(t):
    return vo - g*t

def y(t):
    return y0 + vo*t - 0.5*g*(t**2)

plt.plot(t,y(t))
plt.xlabel('Time(s)')
plt.ylabel('Distance (m)')
plt.title('Position of the Spherical Cow as a Function of Time')
plt.grid()

plt.show()
