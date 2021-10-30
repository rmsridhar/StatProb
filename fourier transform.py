import numpy as np
from scipy.fftpack import fft, ifft
import scipy.stats as stats
import matplotlib.pyplot as plt
import math
x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])
lambda1=2
x=[]
for i in range(5):
    x.append(i)
   # x[i]=lambda1 * math.exp(-lambda1*i)
    x[i]=math.exp(-i)
    print(i)

#np.random.seed(10)
#x= stats.poisson.rvs(loc=18, mu=35, size=10)

print(x)
y = fft(x)
print(y)
plt.plot(x,y)
plt.show()

yinv = ifft(y)
print(yinv)
plt.plot(x,y)
plt.show()
