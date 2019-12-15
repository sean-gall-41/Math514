import numpy as np
from scipy import linalg as la
import cmath as complex
M = np.zeros((3,3))
N = np.eye(3)

A = np.zeros((4,4))

A[0,:]=[1,2,3,0]
A[1,:]=[2,0,2,2]
A[2,:]=[1,-2,1,3]
A[3,:]=[5,1,7,8]

Ai = la.inv(A)
B = np.dot(A,Ai)
C = np.dot(Ai,A)
if np.array_equal(B,C) :
    print('You verified a mathematical identity!')
else :
    print('You don\'t know machine coding! Let\'s try a different method:')
#Got the else block...So how to compare entries of the array as floats?
e = 1.e-14
v =False
while not v:
    for i in np.arange(4):
        for j in np.arange(4):
            print(A[i,j],'\n')
            if np.abs(B[i,j] - C[i,j]) > e:
                v = True
                print('Uh-Oh! entry ',i,' ',j,' is not equivalent!') #are in big trouble if we reach this bramch!
    if i==3 and not v:
        break
    else:
        pass
print('You have successfully determined that A*Ai = Ai*A!!!\n\n',np.transpose(A))
#Found one way to do it...a bit klunky though

#Some complex stuffs
z = 2 - 1j
w = np.complex(2,1)
print('\n',z.imag,z,w)
