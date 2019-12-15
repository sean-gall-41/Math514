from matplotlib import pyplot as plt
import numpy as np
def f(x):
    return 1.0/(1.0 + 25.0*(x**2)) 
x = np.linspace(-1,1,500)

y_true = f(x)
plt.plot(x,y_true,'r',linewidth = 1)

N = 10

xdata = np.linspace(-1,1,N+1)
ydata = f(xdata)
p = np.polyfit(xdata,ydata,N)

y_fit = np.polyval(p,x)
poly_10 = plt.plot(x,y_fit,'b',linewidth = 1)
plt.plot(xdata,ydata,'k.',markersize = 6)

N = 20

xdata = np.linspace(-1,1,N+1)
ydata = f(xdata)
p = np.polyfit(xdata,ydata,N)

y_fit = np.polyval(p,x)
poly_20 = plt.plot(x,y_fit,'g',linewidth = 1)
plt.plot(xdata,ydata,'k.',markersize = 6)
plt.axis([-1,1,-5,5])

N = 40

xdata = np.linspace(-1,1,N+1)
ydata = f(xdata)

p = np.polyfit(xdata,ydata,N)

y_fit = np.polyval(p,x)
poly_40 = plt.plot(x,y_fit,'m',linewidth = 1)
plt.plot(xdata,ydata,'k.',markersize = 6)
#plt.axis([-1,1,-10,10])
plt.axis([-1,1,0,1])
#lh = plt.legend([poly_10,poly_20,poly_40],{'N = 10','N = 20','N = 40'})
#plt.legend(lh,fontsize = 8)

#plt.show()

plt.clf()

y_true = f(x)
plt.plot(x,y_true,'r',linewidth = 1)
#plt.show

N = 10
t = np.linspace(0,np.pi,N+1)
xdata = -np.cos(t)
ydata = f(xdata)

p = np.polyfit(xdata,ydata,N)

y_fit = np.polyval(p,x)

poly_10 = plt.plot(x,y_fit,'b',linewidth = 1)
plt.plot(xdata,ydata,'k.',markersize = 6)
#plt.show()

N = 20
t = np.linspace(0,np.pi,N+1)
xdata = -np.cos(t)
ydata = f(xdata)

p = np.polyfit(xdata,ydata,N)

y_fit = np.polyval(p,x)

poly_20 = plt.plot(x,y_fit,'g',linewidth = 1)
plt.plot(xdata,ydata,'k.',markersize = 6)
#plt.show()

N = 40
t = np.linspace(0,np.pi,N+1)
xdata = -np.cos(t)
ydata = f(xdata)

p = np.polyfit(xdata,ydata,N)

y_fit = np.polyval(p,x)

poly_40 = plt.plot(x,y_fit,'g',linewidth = 1)
plt.plot(xdata,ydata,'k.',markersize = 6)
plt.axis([-1,1,0,1])
plt.show()
