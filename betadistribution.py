import numpy as np
from scipy.stats import beta
from matplotlib import pyplot as plt
import math

# input values where 0<x<1
n=int(input("enter the number of values"))
alpha1=float(input("enter the alpha value"))
beta1 = float(input("enter the beta value"))
x=[]
beta2=[]
m=0
for i in range(0,n):
    x.append(i)
    beta2.append(i)
    x[i]=m
    t=float(math.gamma(alpha1+beta1)* math.pow(x[i],alpha1-1)*math.pow(1-x[i],beta1-1))
    beta2[i]=float(t/(math.gamma(alpha1)*math.gamma(beta1)))
    m=m+0.02
print(beta2)
plt.plot(x,beta2,linewidth=2,color='y')
plt.show()

dist=beta(alpha1,beta1)
plt.plot(x,dist.pdf(x),linewidth=2,color='y')
print(x)
print(dist.pdf(x))
plt.show()

    



