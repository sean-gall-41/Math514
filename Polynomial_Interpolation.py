import numpy as np
from matplotlib import pyplot as plt

def f(x):
    return 1.0 - ((x**2)/(2.0))

def p(x):
    L0 = x**2 -(0.75)*(np.pi)*x + (0.125)*((np.pi)**2)
    L1 = x**2 - (0.5)*(np.pi)*x
#    L2 = ((x)*(x-np.pi/4.0))/((np.pi**2)/(8.0))
    return ((8.0)/((np.pi**2)))*L0 + (16.0)*(1.0/((np.pi**2)))*(1.0/(np.sqrt(2.0)))*L1

N = 500

x = np.linspace(0.0,np.pi/2.0,N)
y = f(x)
z = p(x)
plt.plot(x,y,'g',linewidth = 1)
plt.plot(x,np.cos(x),'b',linewidth = 1)
plt.plot(x,z,'y',linewidth = 1)
plt.show()
