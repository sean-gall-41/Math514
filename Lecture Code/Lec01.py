# First we import some modules:
import numpy as np
from matplotlib import pyplot as plt
def f(x):
    f = 1./8+np.cos(x)**2 - x*np.sin(x)/(1.0+x**2)
    return f
    
x = np.linspace(-20,20,1000)

plt.plot(x,f(x))
plt.plot(x,np.zeros_like(x),'k--')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('A function!')
plt.show()


# Does this simple iteration converge to a solution? How fast? When does it work?

def g(x):
    return x-f(x)

x0 = 1.0 # Initial guess
iterations = 20

x = x0
for k in np.arange(iterations):
    x = g(x)
    print 'x, x-g(x) = ', x, x-g(x)
    plt.plot(k,x,'r.')
plt.show()
    
        
    

