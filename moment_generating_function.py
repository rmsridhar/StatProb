import random
from matplotlib import pyplot as plt
import math
n=100
x=[]
for i in range(n):
     t=random.randrange(-2,2)
     x.append(t)
   # t=random.choice([-2,-1,0,1,2])

print("x=",x)
lambda1=2
y=[]
for i in range(n):
    #print(x[i])
    y.append(i)
    y[i]=(lambda1* math.exp(-1*lambda1*x[i]))
print("y=",y)
plt.plot(x,y,linewidth=2,color="r")
plt.show()
z=[]
v=[]
for i in range(n):
    v.append(i)
    s=random.randrange(-2,2)
    v[i]=s
    z.append(i)
    z[i]=lambda1/(lambda1-v[i])
print("z=",z)
plt.plot(x,z,linewidth=2,color="b")
plt.show()

from scipy.stats import moment
t=moment([1, 2, 3, 4, 5], moment=1)
print(t)
t=moment([1, 2, 3, 4, 5], moment=2)

