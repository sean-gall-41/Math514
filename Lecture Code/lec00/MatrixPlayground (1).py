from numpy import *
from scipy import linalg as la

A = zeros((4,4))
B = zeros((4,4))

A[0,:]=[1,2,3,0]
A[1,:]=[2,0,2,2]
A[2,:]=[1,-2,1,3]
A[3,:]=[5,1,7,8]

for j in arange(1,3):
    B[j,j]=2
    B[j,j+1]=-1
    B[j,j-1]=-1
    
B[0,:]=[2,-1,0,0]
B[3,:]=[0,0,-1,2]

print 'A = '
print A
print ' '

print 'B = '
print B
print ' '

print '|A| = '
print la.det(A)
print ' '

print 'AB = '
print dot(A,B)
print ' '

print '*Element-wise* A*B = '
print A*B
print ' '

print 'A^T = '
print A.T
print ' '

print 'A^{-1} = '
print la.inv(A)
print ' '

print 'A^{-1}A = '
print dot(la.inv(A),A)
print ' '

b=ones((4,1))
x=la.solve(A,b)
print 'Solution to Ax=[1,1,1,1]^T: x = '
print x
print ' '

print 'Ax = '
print dot(A,x)


# Google: "random numbers, python", "plot matrix, python" "count flops, python" Usually a python page or stackoverflow.

#import matplotlib.pyplot as plt
#N = 10
#A = random.rand(N,N)
#plt.pcolor(A)
#plt.colorbar()
#plt.show()
#
#P,L,U = la.lu(A)
#around(P.dot(L).dot(U)-A,14)
#around(L,3)
#
#plt.pcolor(L)
#plt.colorbar()
#plt.show()

import time
Nstart = 200
Nfinal = 1500
Ns = 20
sizes = zeros(((Nfinal-Nstart)/Ns,))
times = zeros(((Nfinal-Nstart)/Ns,))

step = 0
for N in arange(Nstart,Nfinal,Ns):
    
    A = random.rand(N,N)

    start = time.time()    
    P,L,U = la.lu(A)
    end  = time.time()

    sizes[step] = N
    times[step] = end - start
    step += 1

import matplotlib.pyplot as plt
plt.plot(sizes,times,'o')
plt.show()

from scipy import stats
slope, intercept, r_value, p_value, std_err = stats.linregress(log(sizes[-5:]),log(times[-5:]))

print 'slope = ', slope
plt.plot(sizes,times,'o')
plt.plot(sizes,exp(intercept + slope*log(sizes)),'r-')
plt.show()
