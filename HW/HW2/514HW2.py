import numpy as np
from matplotlib import pyplot as plt

#define the tolerance to determine sufficient convergence

tol = 1.0e-12

#A boolean that is flagged false if items not desired to be printed

printWork = True

#Define the functions to be used to test the routines on

def f(x):
    #return x**2*(1.-x)
    #return np.sin(x**2) + 1.02 - np.exp(-x)  
    return (2.0)*(10**29)- (x)*(44**x)
    #return np.exp(x)- x - 1.000000005 Sueli & Mayers #1.5
    #return np.exp(x) - x - 1 Sueli & Mayers #1.6
    
#Define the functions' derivatives as well

def fPrime(x):
    #return 2*x-3*x**2
    return 2*x*np.cos(x**2) + np.exp(-x)
    #return np.exp(x) - 1 Sueli & Mayers #1.5
    #return np.exp(x) - 1 Sueli & Mayers #1.6

########## ~~Definitions of the methods~~ ##########

def Newton(x_0):
    x        = x_0
    x_list   = [x] #Create a list of the iterate values to make plotting easy
    res_list = [abs(f(x))] #create a residual list for plotting
    res      = abs(f(x))  #Note that the residues will be compared to the 
    k_list   = [0]        #tolerance to determine convergence
    n        = 0 #initialize the iterator                     
    while res > tol:
        x = x - f(x)/(fPrime(x)) #The definition of Newton's method
        res = abs(f(x)) #Update the residue before appending to the list
        x_list.append(x)
        res_list.append(res)
        if len(x_list) == 200: #Give a cutoff number of iterates to determine 
                               #sufficient convergence 
            print 'Iteration did not converge within 200 iterates'
            n = n+1 #NOTE: the iterator for the current iteration is updated 
                    #at the end of the current iteration
            k_list.append(n)
            break
        n = n+1
        k_list.append(n) #Update the number of iterates after each iteration
    if printWork:
        fig = plt.figure(1) #Plot the x values against the iterates
        plt.plot(k_list,x_list,'r^')
        plt.title('x values vs the iterates for Newton\'s method')
        plt.xlabel('k')
        plt.ylabel('x value')
        #plt.savefig('C:/Users/Parma_Shon/Desktop/Math 514/HW/HW2/plot_1.png',bbox_inches = 'tight')
        plt.show()
        fig = plt.figure(2) #Plot the residues against the iterates
        plt.plot(k_list,res_list,'ys')
        plt.title('residuals vs the iterates for Newton\'s method')
        plt.xlabel('k')
        plt.ylabel('residual value')
        #plt.savefig('C:/Users/Parma_Shon/Desktop/Math 514/HW/HW2/plot_2.png',bbox_inches = 'tight')
        plt.show
        fig = plt.figure(3) #Plot the log of the residues against the iterates
        plt.plot(k_list,np.log10(res_list),'bo')
        plt.title('log of the residuals vs the iterates for Newton\'s method')
        plt.xlabel('k')
        plt.ylabel('log of residual')
        #plt.savefig('C:/Users/Parma_Shon/Desktop/Math 514/HW/HW2/plot_3.png',bbox_inches = 'tight')
        plt.show()
        print n+1 , x , res #iterates start at 0, so print n + 1 for total 
        
def Secant(x_0,x_1): #Two initial values needed 
    x        = x_0
    x_list   = [x]
    res_list = [abs(f(x))]
    x        = x_1
    x_list.append(x)
    res_list.append(abs(f(x)))
    res = abs(f(x))
    k_list = [0]
    k_list.append(1)
    n = 1
    while res > tol :
        x = x - ((x-x_list[n-1])/(f(x)-f(x_list[n-1])))*f(x) 
        res = abs(f(x))
        x_list.append(x)
        res_list.append(res)
        if len(x_list) == 200:
            print 'Iteration did not converge within 200 iterates'
            n = n+1
            k_list.append(n)
            break
        n = n+1
        k_list.append(n)
    if printWork:
        fig = plt.figure(4) #Plot the x values against the iterates
        plt.plot(k_list,x_list,'r^')
        plt.title('x values vs the iterates for Secant method')
        plt.xlabel('k')
        plt.ylabel('x value')
        #plt.savefig('C:/Users/Parma_Shon/Desktop/Math 514/HW/HW2/plot_4.png',bbox_inches = 'tight')
        plt.show()
        fig = plt.figure(5) #Plot the residues against the iterates
        plt.plot(k_list,res_list,'ys')
        plt.title('residuals vs the iterates for Secant method')
        plt.xlabel('k')
        plt.ylabel('residual value')
        plt.savefig('C:/Users/Parma_Shon/Desktop/Math 514/HW/HW2/plot_5.png',bbox_inches = 'tight')
        plt.show()
        fig = plt.figure(6) #Plot the log of the residues against the iterates
        plt.plot(k_list,np.log10(res_list),'bo')
        plt.title('log of the residuals vs the iterates for Secant method')
        plt.xlabel('k')
        plt.ylabel('log of residual')
        #plt.savefig('C:/Users/Parma_Shon/Desktop/Math 514/HW/HW2/plot_6.png',bbox_inches = 'tight')
        plt.show()
        print n+1 , x , res #iterates start at 0, so print n+1 
                  #to determine total iterations

def Bisection(a,b): #Like the secant method, need two initial values
   c        = (a + b)/2.0 #New value is average of initial two
   c_list   = [c]
   res_list = [abs(f(c))]
   res      = abs(f(c))
   k_list   = [0]
   n        = 0
   while res > tol :
       if f(a)*f(c) < 0: #Condition if f(a) and f(c) are of different sign
           b = c
           c = (a + b)/2.0
           c_list.append(c)
           res = abs(f(c))
           res_list.append(res)
       else : #Condition if f(a) and f(c) are of same sign
           a = c
           c = (a + b)/2.0
           c_list.append(c)
           res = abs(f(c))
           res_list.append(res)
       if len(c_list) == 200:
           print 'Iteration did not converge within 200 iterates'
           n += 1
           k_list.append(n)
           break
       n += 1
       k_list.append(n)
   if printWork:
        fig = plt.figure(7)
        plt.plot(k_list,c_list,'r^')
        plt.title('x values vs the iterates for Bisection method')
        plt.xlabel('k')
        plt.ylabel('x value')
        #plt.savefig('C:/Users/Parma_Shon/Desktop/Math 514/HW/HW2/plot_7.png',bbox_inches = 'tight')
        plt.show()
        fig = plt.figure(8) #Plot the residues against the iterates
        plt.plot(k_list,res_list,'ys')
        plt.title('residuals vs the iterates for Bisection method')
        plt.xlabel('k')
        plt.ylabel('residual value')
        #plt.savefig('C:/Users/Parma_Shon/Desktop/Math 514/HW/HW2/plot_8.png',bbox_inches = 'tight')
        plt.show()
        fig = plt.figure(9) #Plot the log of the residues against the iterates
        plt.plot(k_list,np.log10(res_list),'bo')
        plt.title('log of the residuals vs the iterates for Bisection method')
        plt.xlabel('k')
        plt.ylabel('log of residual')
        #plt.savefig('C:/Users/Parma_Shon/Desktop/Math 514/HW/HW2/plot_9.png',bbox_inches = 'tight')
        plt.show()
   print n , c , res
   
def Illinois(a,b): #Again, this method requires two initial values
    c        = (f(a)*b - f(b)*a)/(f(a)-f(b)) #Alternative definition from:
    #https://en.wikipedia.org/wiki/False_position_method#The_Illinois_algorithm
    c_list   = [c]
    res      = abs(f(c))
    res_list = [res]
    n        = 0
    k_list   = [n]
    side     = 0 #flag that will attain values +/-1 depending on prev iteration
    f_b      = f(b) #Cannot assign values to function calls, make vars instead
    f_a      = f(a)
    while res > tol:
        if f(c)*f(b) > 0:#So that next iteration encapsulates the fixed point
            b = c
            f_b = f(c)#Change the function values accordingly
            if side == -1:#flag raised if prev iteration f(a) was halved
                f_a = f_a/2
            c = (f_a*b - f_b*a)/(f_a-f_b)
            c_list.append(c)
            res = abs(f(c))
            if abs(res - tol) <= tol: #Bug fix for achieving a res of zero.
                res = 1.0e-13 #res < tol anyway, so let res not == zero
            res_list.append(res)
            side = -1
        elif f(a)*f(c) > 0:
            a = c
            f_a = f(c)
            if side == +1:
                f_b = f_b/2
            c = (f_a*b - f_b*a)/(f_a-f_b)
            c_list.append(c)
            res = abs(f(c))
            if abs(res - tol) <= tol:
                res = 1.0e-13
            res_list.append(res)
            side = +1
        else:
            print 'Iteration unexpectedly stopped. Check initial values'
            break
        if len(c_list) == 200:
            print 'Iteration did not converge within 200 iterates'
            n += 1
            k_list.append(n)
            break
        n += 1 
        k_list.append(n)
    if printWork:
        fig = plt.figure(10)
        plt.plot(k_list,c_list,'r^') #plot the sequence values vs iterates
        plt.title('x values vs the iterates for Illinois method')
        plt.xlabel('k')
        plt.ylabel('x value')
        #plt.savefig('C:/Users/Parma_Shon/Desktop/Math 514/HW/HW2/plot_10.png',bbox_inches = 'tight')
        plt.show()
        fig = plt.figure(11) #Plot the residues against the iterates
        plt.plot(k_list,res_list,'ys')
        plt.title('residuals vs the iterates for Illinois method')
        plt.xlabel('k')
        plt.ylabel('residual value')
        #plt.savefig('C:/Users/Parma_Shon/Desktop/Math 514/HW/HW2/plot_11.png',bbox_inches = 'tight')
        plt.show()
        fig = plt.figure(12) #Plot the log of the residues against the iterates
        plt.plot(k_list,np.log10(res_list),'bo')
        plt.title('log of the residuals vs the iterates for Illinois method')
        plt.xlabel('k')
        plt.ylabel('log of residual')
        #plt.savefig('C:/Users/Parma_Shon/Desktop/Math 514/HW/HW2/plot_12.png',bbox_inches = 'tight')
        plt.show()
    print n+1 , c , res #updating iterates at end of iteration => n+1 total
    
##########  ~~Run the routines/plot the functions~~ ##########

Newton(25.0)
#Secant(2.0,2.09)
#Bisection(2.0,2.09)
#Illinois(2.0,2.09)  



        
        
        
    
