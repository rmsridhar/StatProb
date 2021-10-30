import numpy as np
from scipy.stats import beta
from matplotlib import pyplot as plt
import math
a=1
b=10
y=[]
x=[]
for i in range(0,10):
    x.append(i)
    y.append(i)
    x[i]=i
    y[i]=1/(b-a)
plt.plot(x, y)
plt.xlabel('$x$')
plt.ylabel(r'$p(y)$')
plt.title('Uniform Distribution')
plt.show()
