import math
from scipy.stats import hypergeom
import numpy as np
def fact(n):
    if (n==0):
        return 1
      
    if (n==1):
        return 1
    else:
        return (n*fact(n-1))

#print(recursion(3))

M=int(input("enter the population size of M"))
N=int(input("enter the population defective size of N"))
n=int(input("enter the sample size of n"))
r=int(input("enter the sample defective size of r"))
x=[]
for i in range(0,r+1):
    x.append(i)
    print(i)
    ncr=fact(n)/(fact(n-r) * fact(r))
    #print(ncr)
    #print(fact(10))
    McN=fact(M)/(fact(M-N)*fact(N))
    #print(McN)
    M_ncN_r=fact(M-n)/(fact(N-r)* fact((M-n)-(N-r)))
    x[i]=ncr*M_ncN_r/McN
    print(x[i])
p=N/M
print("Expectation of Hypergeometric Distribution")
print(n*p)
print("Variance of Hypergeometric  Distribution")
variance=n*p*(1-p)*(M-N)/(M-1)
print(variance)
print("Standard Deviation")
print(math.sqrt(variance))

# builtin function

[M, n, N] = [10, 3, 4]
rv = hypergeom(M, n, N)
print(rv)      
x = np.arange(0, 3)
pmf_gaskets = rv.pmf(x)
print(pmf_gaskets)
mean,std=hypergeom.stats(M,n,N)
print(mean)
print(std)

    
