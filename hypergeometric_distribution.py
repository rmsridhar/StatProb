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

N=int(input("enter the population size of N"))
M=int(input("enter the population defective size of M"))
n=int(input("enter the sample size of n"))
r=int(input("enter the sample defective size of r"))
x=[]
for i in range(0,r+1):
    x.append(i)
    print(i)
    Ncn=fact(N)/(fact(N-n) * fact(n))
    Mcr=fact(M)/(fact(M-r)*fact(r))
    N_Mcn_r=fact(N-M)/(fact(n-r)* fact((N-M)-(n-r)))
    x[i]=Mcr*N_Mcn_r/Ncn
    print(x[i])
p=M/N
print("Expectation of Hypergeometric Distribution")
print(n*p)
print("Variance of Hypergeometric  Distribution")
variance=n*p*(1-p)*(N-M)/(N-1)
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


    
