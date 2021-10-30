#from scipy.stats import kstest
import numpy as np
import random
import math
a=[5,9,11,16,19]
#b=[12,12,12,12,12]
b=[]
c=[]
cb=[]
f1=[]
f2=[]
s=np.sum(a)
mean1=np.mean(a)
print("mean is ",mean1)
for i in range(len(a)):
        b.append(i)
        b[i]=mean1
c.append(0)
c[0]=a[0]
f1.append(0)
cb.append(0)
cb[0]=mean1
f1[0]=np.absolute(c[0]-cb[0])/s

print(a[0],",",c[0],",",b[0],",",cb[0],",",f1[0])
for i in range(1,len(a)):
        c.append(i)
        cb.append(i)
        f1.append(i)
        c[i]=c[i-1]+a[i]
        cb[i]=cb[i-1]+b[i]
        f1[i]=np.absolute(c[i]-cb[i])/s
        print(a[i],",",c[i],",",b[i],",",cb[i],",",f1[i])
max1=0
for i in range(len(a)):
        if (f1[i]>max1):
                max1=f1[i]
print("calculated Value",max1)
tabulated_value=1.36/math.sqrt(s)
print("Tabulated-value at 5% level of significance",tabulated_value)
if (max1>tabulated_value):
        print("Reject null hypothesis")
else:
        print("Accept null hypothesis")
        

