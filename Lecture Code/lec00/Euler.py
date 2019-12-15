from numpy import *
import matplotlib.pyplot as plt

# Comments like so

T=1
N=100
h=1.0*T/N # WARNING!! 1.0/1000=0.001, but 1/1000=0 (two integers)!!
#Basic integer division (just like in Java)

t=linspace(0.0,T,N) # N uniformly spaced points (N-1 intervals)

def f(y):
    f = 5.0*y*(1.0-y)
    return f

y=zeros(N) # initialize an array
y[0]=2.0 # initial value, index starts at 0

for j in arange(0,N-1):
    y[j+1]=y[j]+h*f(y[j]) # indent the loop


# Plotting
plt.plot(t,y,'r-',linewidth=1) 
plt.show()

    