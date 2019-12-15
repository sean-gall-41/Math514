from matplotlib import pyplot as plt
import math as m
import numpy as np

def Euler(x0,x1,y0,N):
    h = (x1-x0)/N
    x = x0
    y = y0
    for j in np.arange(N):
        y += h*y
    return y
N = 700000
Tol = 0.000001
eapprox = Euler(0.0,1.0,1.0,N)
while abs(eapprox - 2.718281)>Tol:
    N+=100
    print eapprox
    eapprox = Euler(0.0,1.0,1.0,N)
print eapprox, N    

