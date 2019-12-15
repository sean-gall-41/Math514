import numpy as np
from matplotlib import pyplot as plt
#==============================================================================
# PROBLEM 2
#==============================================================================
#Initialize the value of the constant
c = 0.3
#Define the iteration we wish to find fixed points for
def g(x):
    g = 0.5*((x**2) + c)
    return g

#Initialize various initial values for iteration
x_0   = 0.0
y_0   = 1.83
z_0   = -1.0
chi_0 = 1.84

#Initialize the number of iterations to occur
iterations = 20
#Assign initial values to a variable for the iteration
x   = x_0
y   = y_0
z   = z_0
chi = chi_0
plt.plot(0,x,'r^')
plt.plot(0,y,'bo')
plt.plot(0,z,'ys')
#iterate for each initial condition, plot each against 
#the iterator k except chi
for k in np.arange(1,iterations+1):
    x   = g(x)
    y   = g(y)
    z   = g(z)
    plt.plot(k,x,'r^')
    plt.plot(k,y,'bo')
    plt.plot(k,z,'ys')
    if k < 16 :
        chi = g(chi)
        print('k , chi_k = ', k, chi)
print('\nx , y , z for k = 21: ', x, y, z)
plt.title('iteration vs. iterator (k)')
plt.xlabel('iterate (k)')
plt.ylabel('x')
plt.show()
#plt.savefig('C:/Users/Parma_Shon/Desktop/Math 514/HW/plot_1.png',
#            bbox_inches = 'tight')
plt.clf()
#Calculate the solutions of f = x - g(x)
chi_1 = 1.0 - np.sqrt(1.0 - c)
chi_2 = 1.0 + np.sqrt(1.0 - c)
print('\nFor reference: chi_1 , chi_2 = ', chi_1, chi_2, '\n')
#==============================================================================
# Problem 3
#==============================================================================
#definition of recursive relation for problem 3
def h(x):
    h = x - np.power(x , 3.0) - (4.0)*(x**2) + 10.0
    return h

def n(x):
    n = x - h(x)
    return n
#initialize for iteration on h
w_0 = 1.5
#assign the number of iterations to 5
iterations = 5
#create a variable that begins with the initial value
w = w_0
print('\nvalues of the iteration h(x) for which x_0 = 1.5: ')
#Iterate h 5 times and print the results
for k in np.arange(iterations):
    w = h(w)
    print(w)
#This section simply plots n(x) as defined above to show that there
#is only one fixed point, though n approaches 0 near x = -2.75
N = 100   
X = np.linspace(-4.0,2.0,N)
Y = np.zeros(N)
for k in np.arange(0,N):
    Y[k] = n(X[k])
#For clarity, a horizontal line at y = 0 is drawn
plt.plot(X,np.zeros_like(X),'k--')
n_line = plt.plot(X,Y)
plt.setp(n_line,color='r',linewidth=2.0)
plt.title('f(x) vs. x for g in problem 3')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()
#plt.savefig('C:/Users/Parma_Shon/Desktop/Math 514/HW/plot_2.png',
#            bbox_inches = 'tight')
   